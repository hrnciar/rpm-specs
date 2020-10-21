Name:           libmicrodns
Version:        0.1.2
Release:        2%{?dist}
Summary:        Minimal mDNS resolver library

License:        LGPLv2+
URL:            https://github.com/videolabs/libmicrodns
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
%if 0%{?el7}
BuildRequires:  devtoolset-8-toolchain, devtoolset-8-libatomic-devel
%endif


%description
Minimal mDNS resolver (and announcer) library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup
%if 0%{?rhel}
# lower the meson requirement there
sed -i -e 's/0.50.0/0.47.2/' meson.build
sed -i -e "/subdir('examples')/d" meson.build
%endif


%build
%if 0%{?el7}
. /opt/rh/devtoolset-8/enable
%endif
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libmicrodns.so.0*

%files devel
%{_includedir}/microdns
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-1
- Update to 0.1.2
- Switch to meson

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Wed Feb 14 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.0.8-1
- Initial spec file
