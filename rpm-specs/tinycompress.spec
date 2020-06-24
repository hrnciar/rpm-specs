Name:          tinycompress
Version:       1.2.2
Release:       1%{?dist}
Summary:       A library for compress audio offload in alsa
License:       BSD and LGPLv2
URL:           http://alsa-project.org/
Source0:       ftp://ftp.alsa-project.org/pub/tinycompress/%{name}-%{version}.tar.bz2

BuildRequires: gcc

%description
tinycompress is a library for compress audio offload in alsa

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package utils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilies for testing of compressed audio with %{name}.

%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}/tinycompress*
%{_libdir}/*.so
%{_libdir}/pkgconfig/tinycompress.pc

%files utils
%{_bindir}/cplay
%{_bindir}/crecord

%changelog
* Wed Feb 19 2020 Jaroslav Kysela <perex@perex.cz> 1.2.2-1
- 1.2.2 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.7-1
- 1.1.7 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.6-1
- 1.1.6 release

* Fri Mar  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.5-3
- Add gcc BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.5-1
- 1.1.5 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.4-1
- 1.1.4 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-1
- 1.1.3 release

* Fri Apr  1 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-1
- 1.1.1 release

* Sat Feb 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-2
- Minor updates

* Fri Nov 13 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-1
- Initial package
