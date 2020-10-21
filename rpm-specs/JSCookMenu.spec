Name:		JSCookMenu
Summary:	JavaScript GUI-like web menus
Version:	2.0.4
Release:	20%{?dist}
License:	MIT and Public Domain
URL:		http://jscook.yuanheng.org/JSCookMenu/
Source0:	http://downloads.sourceforge.net/jscook/jscookmenu-%{version}.zip
Source1:	http://downloads.sourceforge.net/jscook/ThemeGray-1.0.zip
Source2:	http://downloads.sourceforge.net/jscook/ThemeIE-1.1.zip
Source3:	http://downloads.sourceforge.net/jscook/ThemeMiniBlack-1.1.zip
Source4:	http://downloads.sourceforge.net/jscook/ThemeOffice-1.1.zip
Source5:	http://downloads.sourceforge.net/jscook/ThemeOffice2003-1.1.zip
Source6:	http://downloads.sourceforge.net/jscook/ThemePanel-1.1.zip
Source10:	JSCookMenu_theme_license_clarification.mail.txt
Requires:	httpd >= 2.4
Buildarch:	noarch
BuildRequires:	dos2unix

%description
  JSCookMenu is a powerful menu script written in JavaScript that can
mimic complex menus found in popular GUI Applications. It is relatively
simple and easy to use. Creating a new theme requires some patience,
but rarely does one has to write one since some good ones are provided. 
  The following features are implemented:
* Supports both horizontal and vertical menus.
* Supports relative positioning.
* Supports different menus with different themes in the same web page.
* Eases the menu creation process with a menu builder.
* Special effects such as sliding and fading in/out is available.
* APIs for JavaScript developers.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -c
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%setup -q -D -T -a 3
%setup -q -D -T -a 4
%setup -q -D -T -a 5
%setup -q -D -T -a 6
cp -a "%{SOURCE10}" .


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Make sure source lines end with a newline.

find . -type f \( -name "*.js" -o -name "*.css" \) | xargs dos2unix


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

rm -rf "${RPM_BUILD_ROOT}"

#	Install directories.

install -p -d -m 755 "${RPM_BUILD_ROOT}/%{_datadir}/%{name}/"
install -p -d -m 755 "${RPM_BUILD_ROOT}/%{_sysconfdir}/httpd/conf.d"


#	Install files.

cp -a * "${RPM_BUILD_ROOT}/%{_datadir}/%{name}/"


#	Include it in web server configuration.

cat > "${RPM_BUILD_ROOT}/%{_sysconfdir}/httpd/conf.d/%{name}.conf" << 'EOF'
Alias /%{name} %{_datadir}/%{name}
<Directory %{_datadir}/%{name}>
	Options		None
	AllowOverride	None
	Require		local
</Directory>
EOF

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%defattr(0644, root, root, 0755)
%doc JSCookMenu_theme_license_clarification.mail.txt
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf


#-------------------------------------------------------------------------------
%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

#-------------------------------------------------------------------------------

* Tue Apr 24 2012 Patrick Monnerat <pm@datasphere.ch> 2.0.4-6
- Upgrade httpd configuration file to Apache 2.4 syntax.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May  7 2010 Patrick Monnerat <pm@datasphere.ch> 2.0.4-3
- Fix summary typo.
- Supress httpd reload on post and postun.

* Mon Jan 25 2010 Patrick Monnerat <pm@datasphere.ch> 2.0.4-2
- Themes license clarification e-mail added in documentation.

* Wed Jun 10 2009 Patrick Monnerat <pm@datasphere.ch> 2.0.4-1
- Initial RPM spec file.
