%define nodoka_dir %{_datadir}/themes/Nodoka

Name:           nodoka-theme-gnome
Version:        0.3.90
Release:        20%{?dist}
Summary:        The Nodoka Theme Pack for Gnome

License:        GPLv2
URL:            http://hosted.fedoraproject.org/projects/nodoka

# can get on a wiki, see URL
Source0:        %{name}-%{version}.tar.gz 

BuildArch:      noarch

Requires:       gtk-nodoka-engine >= 0.3.1.1
Requires:       nodoka-metacity-theme
Requires:       fedora-icon-theme
Requires:       notification-daemon-engine-nodoka

%description
The Nodoka Theme Pack for Gnome make use of Nodoka Metacity theme, Nodoka gtk2
theme and Echo Icon set.


# subpackage has inverse relationship to the main package
# the reason is that metacity theme is a part of the whole theme and as its
# in one source with the metatheme the nodoka-theme-gnome seems more rational
# to be the name of the main package

%package -n     nodoka-metacity-theme
Summary:        The Nodoka theme for Metacity 

# needed for dir ownership
Requires:       nodoka-filesystem

%description -n nodoka-metacity-theme
The Nodoka theme for metacity. A clean theme featuring soft gradients and 
Echoey look and feel.

%package -n     nodoka-filesystem
Summary:        The directory infrastructure for Nodoka

# Require the %{_datadir}/themes directory
Requires:       filesystem
Conflicts:      gtk-nodoka-engine < 0.7.0-2

%description -n nodoka-filesystem
The directory infrastructure needed by various Nodoka packages.

%prep
%setup -q
echo 'NotificationTheme=nodoka' >> Nodoka/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -Dp -m 0644 Nodoka/index.theme                             $RPM_BUILD_ROOT/%{nodoka_dir}/index.theme
%{__install} -Dp -m 0644 Nodoka/metacity-1/button_close.png             $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/button_close.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/button_maximize.png          $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/button_maximize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/button_minimize.png          $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/button_minimize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/menu_button_close.png        $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/menu_button_close.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/menu_button_maximize.png     $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/menu_button_maximize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/menu_button_minimize.png     $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/menu_button_minimize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/metacity-theme-1.xml         $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/metacity-theme-1.xml


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{nodoka_dir}/index.theme

%files -n nodoka-metacity-theme
%{nodoka_dir}/metacity-1

%files -n nodoka-filesystem
%dir %{nodoka_dir}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 20 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.90-2
- Split nodoka-filesystem subpackage so that Nodoka package need not 
  to depend on gtk-nodoka-engine
- Add NotificationTheme=nodoka to metatheme (rhbz #447085)
- Drop metacity requires (rhbz #398521)

* Sun Feb 10 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.90-1
- New release 0.4 beta

* Thu Sep 27 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-2
- Require fedora-icon-theme instead of redhat-artwork (rhbz #309631)

* Thu Sep 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-1.fc8.1
- fix dir name

* Thu Sep 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-1
- new version, reworked gradients in metacity theme

* Sat Aug 11 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.2-1
- new version, change used icon set to fedora (in redhat-artwork pkg)

* Thu Aug 09 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-4
- update License: field to GPLv2

* Sat Aug 04 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-3
- fix dir ownership
- add a comment about the inverse relationship of the main package to the 
  subpackage
- add a comment about upstream sources location

* Fri Jul 27 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-2
- remove empty %%dir for nodoka-metacity-theme
- fix the %%description to be more sane

* Fri Jul 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-1
- split metacity and metatheme into separate package in upstream
