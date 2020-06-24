Name:           open-eid
Version:        17.12
Release:        7%{?dist}
Summary:        Meta-package for Estonian Electronic Identity Software

License:        LGPLv2+
URL:            http://www.ria.ee
BuildArch:      noarch

Requires:       qdigidoc
Requires:       firefox-pkcs11-loader
Requires:       webextension-token-signing
Provides:       estonianidcard = %{version}-%{release}
Obsoletes:      estonianidcard <= 3.12.0-2

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running ID-card utilities.

%prep
%setup -c -T


%build


%install


%files


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Germano Massullo <germano@germanomassullo.org> - 17.12-4
- removed Requires: qesteidutil

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Germano Massullo <germano.massullo@gmail.com> - 17.12-2
- rebuilt

* Fri Mar 02 2018 Germano Massullo <germano.massullo@gmail.com> - 17.12-1
- 17.12-1 release

* Tue Feb 02 2016 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.0-1
- Bump version number

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.1-2
- Remove doc since there is no documentation
- Remove opensc and pcsc-lite package from requires

* Tue Mar  4 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.1-1
- Initial meta-package

