%global npmname zeropad

Name:           nodejs-%{npmname}
Version:        1.1.0
Release:        4%{?dist}
Summary:        Zeropad your integers with optional n-length padding

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

# Add tests to npm archive.
# Thanks eclipseo for porting tests to nodejs 10!
# https://github.com/radiovisual/zeropad/pull/1
Source1:        https://raw.githubusercontent.com/radiovisual/zeropad/3bd15b69384cc74d55ac2c4c870728b74d1ff9a9/test.js

BuildRequires:  nodejs-packaging

BuildRequires:  mocha
BuildRequires:  nodejs-negative-zero

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Zeropad your integers with optional n-length padding.

%prep
%autosetup -n package

# Copy tests into build directory.
cp %SOURCE1 .

%nodejs_fixdep negative-zero

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
mocha

%files
%{nodejs_sitelib}/%{npmname}/
%license license.md
%doc readme.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Initial package.
