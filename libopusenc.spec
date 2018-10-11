#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	High-level Opus encoding library
Summary(pl.UTF-8):	Wysokopoziomowa biblioteka do kodowania w formacie Opus
Name:		libopusenc
Version:	0.2.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz
# Source0-md5:	f038ea0f4168d184c76b42d293697c57
URL:		http://opus-codec.org/
BuildRequires:	doxygen
BuildRequires:	opus-devel >= 1.1
Requires:	opus >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libopusenc library provides a high-level API for encoding .opus
files. libopusenc depends only on libopus.

%description -l pl.UTF-8
Biblioteka libopusenc udostępnia wysokopoziomowe API do kodowania
plików .opus. libopusenc zależy tylko od libopus.

%package devel
Summary:	Header files for libopusenc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libopusenc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	opus-devel >= 1.1

%description devel
Header files for libopusenc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libopusenc.

%package static
Summary:	Static libopusenc library
Summary(pl.UTF-8):	Statyczna biblioteka libopusenc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libopusenc library.

%description static -l pl.UTF-8
Statyczna biblioteka libopusenc.

%package apidocs
Summary:	API documentation for libopusenc library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libopusenc
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libopusenc library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libopusenc.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libopusenc.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libopusenc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md
%attr(755,root,root) %{_libdir}/libopusenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopusenc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopusenc.so
%{_includedir}/opus/opusenc.h
%{_pkgconfigdir}/libopusenc.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopusenc.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/{search,*.css,*.html,*.js,*.png}
