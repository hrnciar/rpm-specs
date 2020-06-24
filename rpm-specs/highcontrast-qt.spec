Name:           highcontrast-qt
Version:        0.1
Release:        9%{?dist}
License:        GPLv2+ and MIT
Summary:        HighContrast theme for Qt-based applications

Url:            https://github.com/MartinBriza/highcontrast-qt
Source0:        https://github.com/MartinBriza/highcontrast-qt/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel

Requires:       highcontrast-qt5

%description
Theme to let Qt applications fit nicely into Fedora Workstation


%package -n highcontrast-qt4
Summary:        HighContrast Qt4 theme
Requires:       qt5-qtbase

%package -n highcontrast-qt5
Summary:        HighContrast Qt5 theme
Requires:       qt5-qtbase


%description -n highcontrast-qt4
HighContrast theme variant for applications utilizing Qt4

%description -n highcontrast-qt5
HighContrast theme variant for applications utilizing Qt5


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -p "%{_target_platform}-qt4"
pushd "%{_target_platform}-qt4"
%{cmake} -DUSE_QT4=true ..
popd

mkdir -p "%{_target_platform}-qt5"
pushd "%{_target_platform}-qt5"
%{cmake} ..
popd

make %{?_smp_mflags} -C "%{_target_platform}-qt4"
make %{?_smp_mflags} -C "%{_target_platform}-qt5"


%install
make install/fast DESTDIR=%{buildroot} -C "%{_target_platform}-qt4"
make install/fast DESTDIR=%{buildroot} -C "%{_target_platform}-qt5"


%files -n highcontrast-qt4
%license LICENSE.GPL2
%doc README.md
%{_qt4_plugindir}/styles/highcontrast.so

%files -n highcontrast-qt5
%license LICENSE.GPL2
%doc README.md
%{_qt5_plugindir}/styles/highcontrast.so

%files

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Martin Briza <mbriza@redhat.com> - 0.1-1
- Initial build
