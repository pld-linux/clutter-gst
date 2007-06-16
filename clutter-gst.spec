Summary:	Library integrating clutter with GStreamer
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GStreamerem
Name:		clutter-gst
Version:	0.1.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter-gst/0.1/%{name}-%{version}.tar.gz
# Source0-md5:	13fb455ab14c32a06758ed02076f7fa5
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	gstreamer-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc-common
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
