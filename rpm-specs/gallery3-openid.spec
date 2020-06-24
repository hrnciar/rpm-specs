Name:           gallery3-openid
Version:        2.0
Release:        0.14.beta%{?dist}
Summary:        OpenID support for Gallery3

License:        GPLv2+
URL:            http://kott.fm/tomek/plugins-extensions/openid/
Source0:        http://kott.fm/tomek/wp-content/uploads/2012/05/openid-%{version}-beta.zip
Patch0:         0001-add-fedora.patch

BuildRequires:  php-lightopenid
BuildRequires:  openid-selector
Requires:       gallery3
Requires:       php-lightopenid >= 0.6-2
Requires:       openid-selector
BuildArch:      noarch

%description
Adds OpenID authentication support to Gallery3


%prep
%setup -q -n openid
%patch0 -p1

%build
rm -f lib/openid.php
rm -rf lib/openid-selector
ln -s %{_datadir}/php/lightopenid/openid.php lib/openid.php
ln -s %{_datadir}/openid-selector lib/openid-selector

%install
mkdir -p %{buildroot}%{_datadir}/gallery3/modules/openid
cp -pR * %{buildroot}%{_datadir}/gallery3/modules/openid

%files
%{_datadir}/gallery3/modules/openid

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.0-0.4.beta
- Update for new path to lightopenid

* Sun Oct 13 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.0-0.3.beta
- Add Fedora provider

* Tue Oct 01 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 2.0-0.2.beta
- Add -p flag to cp
- Split lightopenid and openid-selector

* Tue Oct 01 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 2.0-0.1.beta
- Initial packaging

