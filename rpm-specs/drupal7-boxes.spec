%{?drupal7_find_provides_and_requires}

%global module boxes

Name:          drupal7-%{module}
Version:       1.2
Release:       11%{?dist}
Summary:       Provides exports for custom blocks and spaces integration

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

Requires:      drupal7-ctools
#Requires:      drupal7(ctools)
# phpcompatinfo (computed from version 1.2)
Requires:      php-pcre

%description
Boxes module is a re-implementation of the custom blocks (boxes) that the core
block module provides. It is a proof of concept for what a re-worked block
module could do.

The module assumes that custom blocks are configuration, and not content. This
means that it is a reasonable action to ask for all blocks at one time, this is
in fact exactly what the core block module does.

Boxes provides an inline interface for editing blocks, allowing you to change
the contents of blocks without going to an admin page.

Boxes provides exportables for its blocks via the (required) Chaos tools module.
This allows modules to provide blocks in code that can be overwritten in the UI.

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.txt
%{drupal7_modules}/%{module}
%exclude %{drupal7_modules}/%{module}/*.txt


%changelog
* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-11
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jul 20 2014 hawn Iwinski <shawn.iwinski@gmail.com> - 1.2-1
- Updated to 1.2 (BZ #1114975; release notes https://www.drupal.org/node/2295431)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-2
- Updated for drupal7-rpmbuild 7.22-5

* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Initial package
