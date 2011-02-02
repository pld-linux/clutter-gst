Summary:	Library integrating clutter with GStreamer
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GStreamerem
Name:		clutter-gst
Version:	1.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://source.clutter-project.org/sources/clutter-gst/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	1048815f0c9152edbfdc59a94d0e3b87
Patch0:		%{name}-link.patch
Patch1:		%{name}-ver.patch
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 0.6.8
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python
Requires:	clutter >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with GStreamer.

%description -l pl.UTF-8
Biblioteka integrująca clutter z GStreamerem.

%package devel
Summary:	Header files for clutter-gst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-gst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.2.0
Requires:	gstreamer-devel >= 0.10
Requires:	gstreamer-plugins-base-devel >= 0.10

%description devel
Header files for clutter-gst library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-gst.

%package static
Summary:	Static clutter-gst library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-gst
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-gst library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-gst.

%package apidocs
Summary:	clutter-gst API documentation
Summary(pl.UTF-8):	Dokumentacja API clutter-gst
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter-gst API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API clutter-gst.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libclutter-gst-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-gst-1.0.so.0
%{_libdir}/girepository-1.0/ClutterGst-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gst-1.0.so
%{_libdir}/libclutter-gst-1.0.la
%{_includedir}/clutter-1.0/clutter-gst
%{_datadir}/gir-1.0/ClutterGst-1.0.gir
%{_pkgconfigdir}/clutter-gst-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gst-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
