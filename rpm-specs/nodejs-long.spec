%global npmname long

Name:           nodejs-%{npmname}
Version:        4.0.0
Release:        6%{?dist}
Summary:        Long class for representing a 64-bit two's-complement integer

License:        ASL 2.0
URL:            https://www.npmjs.com/package/%{npmname}

# NPM does not have tests.
Source0:        https://github.com/dcodeIO/long.js/archive/%{version}/%{npmname}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
A Long class for representing a 64 bit two's-complement integer value derived
from the Closure Library for stand-alone use and extended with unsigned
support.

%prep
%autosetup -n long.js-%{version}

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a src/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node tests

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 4.0.0-1
- Initial package.
