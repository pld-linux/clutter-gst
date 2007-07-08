Summary:	Library integrating clutter with GStreamer
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GStreamerem
Name:		clutter-gst
Version:	0.3.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter-gst/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	8c163232367adca8fce796a149af7989
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	clutter-devel >= 0.2
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
Requires:	clutter-devel >= 0.2
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

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libclutter-gst-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gst-*.so
%{_libdir}/libclutter-gst-*.la
%{_includedir}/clutter-gst-*
%{_pkgconfigdir}/clutter-gst-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gst-*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
