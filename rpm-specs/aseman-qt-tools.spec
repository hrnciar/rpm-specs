%global channel stable

# Since Qt 5.7.0 is not needed
%{!?_qt5_qmldir:%global _qt5_qmldir %%{_qt5_archdatadir}/qml}

Name:           aseman-qt-tools
Version:        1.0.0
Release:        15%{?dist}
Summary:        Shared tools and functions, used in the aseman's projects

License:        GPLv3+
URL:            https://github.com/Aseman-Land/%{name}
Source0:        %{url}/archive/v%{version}-%{channel}/%{name}-%{version}.tar.gz

# https://github.com/Aseman-Land/aseman-qt-tools/commit/47412ddb26acf227ee6cb6950f6e9ded01f3375c
Patch0001:      0001-add-plugin-definition-in-qmldir.patch
# https://github.com/Aseman-Land/aseman-qt-tools/commit/8e21628b38078d0b25b37d6fbd853dd2fd3002ad
Patch0002:      0001-chmod-x-on-all-sources.patch

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qtkeychain-qt5-devel

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}-%{channel} -p1
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %qmake_qt5 ..       \
      QT+=widgets     \
      QT+=multimedia  \
      QT+=dbus        \
      QT+=sensors     \
      QT+=positioning \
      %{nil}
popd
%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%license LICENSE
%{_qt5_qmldir}/AsemanTools/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 24 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-5
- Trivial fixes

* Sun Jul 24 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-4
- Replace BR with proper qt5-qtdeclarative

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-3
- Remove executable flag from files

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-2
- Backport critical patch

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-1
- Initial package
