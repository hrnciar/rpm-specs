Name:          libsoc
Version:       0.8.2
Release:       16%{?dist}
Summary:       Interface with common SoC peripherals through generic kernel interfaces 

License:       LGPLv2+
URL:           https://github.com/jackmitch/libsoc
Source0:       https://github.com/jackmitch/libsoc/archive/%{version}.tar.gz

BuildRequires: libtool autoconf automake
BuildRequires: python3-devel

%description
libsoc is a C library for interfacing with common SoC peripherals through 
generic kernel interfaces.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package -n    python3-libsoc
Summary:       A Python 3 interface to libsoc
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libsoc
Python 3 bindings for libsoc for gpio and i2c

%prep
%setup -q

%build
autoreconf -vif
%configure --disable-static --enable-python=3 --with-board-configs

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license LICENCE
%doc README.md ChangeLog
%{_libdir}/*.so.*
%{_datadir}/libsoc

%files devel
%{_includedir}/libsoc*
%{_libdir}/pkgconfig/libsoc.pc
%{_libdir}/*.so

%files -n python3-libsoc
%{python3_sitearch}/libsoc/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-15
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-12
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-8
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-1
- Update to 0.8.2

* Mon May 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.1-1
- Update to 0.8.1
- Build new python3 bindings

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-1
- Update to 0.7.1

* Sat Nov  7 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-1
- Update to 0.7

* Tue Oct 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.5-1
- Initial package
