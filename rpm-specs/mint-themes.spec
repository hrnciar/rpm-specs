Name:           mint-themes
Epoch:          1
Version:        1.8.6
Release:        2%{?dist}
Summary:        Mint themes

License:        GPLv3+
URL:            https://github.com/linuxmint/%{name}
Source0:        http://packages.linuxmint.com/pool/main/m/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  sassc

%description
A collection of mint themes.

%package -n     mint-y-theme
Summary:        The Mint-Y theme 
Requires:       mint-y-icons

%description -n	mint-y-theme
The Mint-Y theme.  This theme is based on the Arc theme.

%package -n     mint-themes-gtk3
Summary:        Mint themes for GTK3
Requires:       mint-themes
Requires:       mint-x-icons

%description -n	mint-themes-gtk3
A collection of mint themes for GTK3.

%package -n	cinnamon-themes
Summary:        Mint themes for GTK3 
Requires:       filesystem
Requires:       mint-themes-gtk3
Requires:       mint-y-theme

%description -n	cinnamon-themes
Collection of the best themes available for Cinnamon


%prep
%autosetup -p1 -n %{name}

%{__sed} -i -e 's@Ubuntu@Noto Sans@g' files/usr/share/themes/Linux\ Mint/cinnamon/cinnamon.css

%build
make

%install
%{__cp} -pr usr/ %{buildroot}
%fdupes -s %{buildroot}


%files
%license debian/copyright
%doc debian/changelog
%dir %{_datadir}/themes/Mint-X*/
%dir %{_datadir}/themes/Mint-X*/gtk-3.0/
%{_datadir}/themes/Mint-X*/index.theme
%{_datadir}/themes/Mint-X*/metacity-1/
%{_datadir}/themes/Mint-X/xfce-notify-4.0/
%{_datadir}/themes/Mint-X/xfwm4/
%{_datadir}/themes/Mint-X*/gtk-2.0/
%{_datadir}/themes/Mint-X-compact/xfwm4/

%files -n mint-y-theme
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-Y*

%files -n mint-themes-gtk3
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint-X*/gtk-3.0/*

%files -n cinnamon-themes
%license debian/copyright
%doc debian/changelog
"%{_datadir}/themes/Linux Mint"
%{_datadir}/themes/Mint-X*/cinnamon/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Leigh Scott <leigh123linux@gmail.com> - 1:1.8.6-1
- Update to 1.8.6

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 1:1.8.5-1
- Update to 1.8.5

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1:1.8.4-1
- Update to 1.8.4

* Mon Apr 20 2020 Leigh Scott <leigh123linux@gmail.com> - 1:1.8.4-0.1.20200415git2512422
- Update to git snapshot

* Wed Feb 26 2020 Leigh Scott <leigh123linux@googlemail.com> - 1:1.8.3-3
- Use sassc precompiled source 

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:1.8.3-1
- Update to 1.8.3

* Mon Aug 12 2019 Leigh Scott <leigh123linux@gmail.com> - 1:1.8.2-1
- Update to 1.8.2
- Revert upstream Ubuntu font change

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:1.8.1-1
- Update to 1.8.1

* Fri Jul 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:1.8.0-1
- Update to 1.8.0

* Tue Jul 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.9-1
- Update to 1.7.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.7-1
- Update to 1.7.7

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.4-1
- Update to 1.7.4

* Wed Nov 14 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.4-0.2.20181112gitb94b890
- Update snapshot

* Mon Nov 05 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.4-0.1.20181103gitcc5ba69
- Update to git snapshot

* Sun Nov 04 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.3-1
- Update to 1.7.3

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.2-1
- Update to 1.7.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.7.1-1
- Update to 1.7.1

* Thu Jun 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.8-1
- Update to 1.6.8

* Sat Jun 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.7-1
- Update to 1.6.7

* Tue May 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.6-1
- Update to 1.6.6

* Mon May 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.5-1
- Update to 1.6.5

* Mon May 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.4-1
- Update to 1.6.4

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.3-1
- Update to 1.6.3

* Fri Apr 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.2-1
- Update to 1.6.2

* Sun Apr 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.2-0.5.20180408git0a7f930
- Update to git snapshot

* Fri Apr 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.2-0.4.20180405git295b819
- Update to git snapshot

* Tue Apr 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.2-0.3.20180403gitc402169
- Update to git snapshot

* Tue Apr 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.2-0.2.20180403git1e2c2db
- Update to git snapshot

* Mon Apr 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.2-0.1.20180402git2e06d4d
- Update to git snapshot
- Add build requires python3

* Wed Feb 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:1.6.1-1
- Update to 1.6.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.5.0-1
- Initial import (#1529555)

* Thu Dec 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.5.0-0.1
- Initial rpm release (#1529555)
