Name:           deepin-icon-theme
Version:        15.12.71
Release:        3%{?dist}
Summary:        Icons for the Deepin Desktop Environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}_fix-makefile.patch
BuildArch:      noarch
BuildRequires:  /usr/bin/python
BuildRequires:  gtk-update-icon-cache
BuildRequires:  xorg-x11-apps
Requires:       papirus-icon-theme

%description
%{summary}.

%prep
%autosetup -p1

%build
make

%install
%make_install PREFIX=%{_prefix}

%post
touch --no-create %{_datadir}/icons/deepin &>/dev/null || :
touch --no-create %{_datadir}/icons/deepin-dark &>/dev/null || :
touch --no-create %{_datadir}/icons/Sea &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/deepin &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin &>/dev/null || :
  touch --no-create %{_datadir}/icons/deepin-dark &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin-dark &>/dev/null || :
  touch --no-create %{_datadir}/icons/Sea &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Sea &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin-dark &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Sea &>/dev/null || :

%files
%license LICENSE
%{_datadir}/icons/hicolor/*/status/*.svg
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/icons/deepin-dark/
%{_datadir}/icons/deepin/
%{_datadir}/icons/Sea/
%ghost %{_datadir}/icons/deepin/icon-theme.cache
%ghost %{_datadir}/icons/deepin-dark/icon-theme.cache
%ghost %{_datadir}/icons/Sea/icon-theme.cache

%changelog
* Thu Jan 30 2020 Petr Viktorin <pviktori@redhat.com> - 15.12.71-3
- Require /usr/bin/python to remove dependency on Python 2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 15.12.71-1
- Release 15.12.71

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr  3 2019 Robin Lee <cheeselee@fedoraproject.org> - 15.12.68-2
- Requires papirus-icon-theme
- Ghost owning cache files
- Create cache for deepin-dark theme

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 15.12.68-1
- Update to 15.12.68

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 15.12.67-1
- Update to 15.12.67

* Fri Nov 30 2018 mosquito <sensor.wen@gmail.com> - 15.12.65-1
- Update to 15.12.65

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 15.12.64-1
- Update to 15.12.64

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 15.12.59-1
- Update to 15.12.59

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 15.12.58-1
- Update to 15.12.58

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 15.12.52-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 15.12.52-1
- Update to 15.12.52

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 15.12.49-1
- Update to 15.12.49

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 15.12.46-1
- Update to 15.12.46

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 15.12.42-1.git59ca728
- Update to 15.12.42

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 15.12.33-1.git2f50a33
- Update to 15.12.33

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 15.12.32-1.git69bcc88
- Update to 15.12.32

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
