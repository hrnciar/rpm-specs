Name:           lxqt-build-tools
Version:        0.7.0
Release:        4%{?dist}
Summary:        Packaging tools for LXQt

License:        BSD
URL:            http://lxqt.org/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  glib2-devel
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

Requires:       %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0

%description
Various packaging tools and scripts for LXQt applications.


%prep
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
%autosetup -p1
%{__mkdir} -p %{_target_platform}
%if 0%{?el7}
EOF
%endif


%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

%cmake3 -DPULL_TRANSLATIONS=NO

%cmake_build


%if 0%{?el7}
EOF
%endif

%install
%cmake_install

%files
%license BSD-3-Clause
%doc CHANGELOG README.md
%{_datadir}/cmake/%{name}
%{_bindir}/lxqt-transupdate


%changelog
* Tue Aug 11 2020 Zamir SUN <sztsian@gmail.com> - 0.7.0-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 0.6.0-3
- Improve compatibility with epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.6.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.2-1
- new version (0.3.2)
- patch to make package noarch'ed removed, has been upstreamed

* Fri Jan 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-3
- Build out-of-tree

* Fri Jan 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.3.1-2
- Update Patch0 to make the whole package noarch'ed
- Add `BuildArch: noarch`
- Clean trailing whitespaces

* Mon Jan  2 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.1-1
- initial package
