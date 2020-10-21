%define __cmake_in_source_build 1

%global cmake_build_dir build-cmake
%global debug_package %{nil}
%bcond_without qt4
%bcond_without qt5

Name:           se-sandbox-runner
Version:        1.7.14
Release:        13%{?dist}
Summary:        Qt wrapper for SELinux Sandbox
License:        GPLv2+
Source0:        https://github.com/F1ash/%{name}/archive/%{version}.tar.gz
URL:            https://github.com/F1ash/%{name}

Requires:       xdg-utils
Requires:       hicolor-icon-theme
Requires:       policycoreutils-sandbox
%if (0%{?fedora} >= 20)
Requires:       selinux-policy-sandbox
%endif
Conflicts:      se-sandbox-runner
%if %with qt4
BuildRequires:  qt4-devel
%endif
%if %with qt5
BuildRequires:  qt5-qtbase-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  cmake

%description
Qt wrapper for SELinux Sandbox.
This application runs and controls the configured jobs, running in a sandbox.
Job settings are saved in the application's configuration.

%package        qt4
Summary:        Qt4 wrapper for SELinux Sandbox

%description    qt4
Qt4 wrapper for SELinux Sandbox.
This application runs and controls the configured jobs, running in a sandbox.
Job settings are saved in the application's configuration.

%package        qt5
Summary:        Qt5 wrapper for SELinux Sandbox

%description    qt5
Qt5 wrapper for SELinux Sandbox.
This application runs and controls the configured jobs, running in a sandbox.
Job settings are saved in the application's configuration.

%prep
%setup -q

%build
%if %with qt4
mkdir %{cmake_build_dir}-qt4
pushd %{cmake_build_dir}-qt4
      %cmake ..
      %{make_build}
popd
%endif
%if %with qt5
mkdir %{cmake_build_dir}-qt5
pushd %{cmake_build_dir}-qt5
      %cmake -DBUILD_QT_VERSION=5 ..
      %{make_build}
popd
%endif

%install
%if %with qt4
pushd %{cmake_build_dir}-qt4
      %{make_install}
popd
%endif
%if %with qt5
pushd %{cmake_build_dir}-qt5
      %{make_install}
popd
%endif

%check
%if %with qt4
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt4.desktop
%endif
%if %with qt5
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt5.desktop
%endif

%if %with qt4
%files qt4
%doc README.md Changelog
%license COPYING
%{_bindir}/%{name}-qt4
%{_datadir}/applications/%{name}-qt4.desktop
%{_datadir}/icons/hicolor/256x256/apps/applications-safety-selinux.png
%endif
%if %with qt5
%files qt5
%doc README.md Changelog
%license COPYING
%{_bindir}/%{name}-qt5
%{_datadir}/applications/%{name}-qt5.desktop
%{_datadir}/icons/hicolor/256x256/apps/applications-safety-selinux.png
%endif

%changelog
* Tue Sep 20 2020 Jeff Law <law@redhat.com> - 1.7.14-13
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec  5 2015 Fl@sh <kaperang07@gmail.com> - 1.7.14-1
- added hicolor-icon-theme R;
- removed sandbox-runner-data R;
- added app icon to %%files;
- version updated;

* Fri Nov  6 2015 Fl@sh <kaperang07@gmail.com> - 1.6.14-1
- added %%license field to %%files;
- version updated;

* Tue Feb 10 2015 Fl@sh <kaperang07@gmail.com> - 1.6.13-1
- version updated;

* Sat Dec 13 2014 Fl@sh <kaperang07@gmail.com> - 1.6.12-4
- fixed for both qt4 and qt5 building;
- release updated;
- spec %%changelog cleared;
