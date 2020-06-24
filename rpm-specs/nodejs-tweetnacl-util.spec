%global npmname tweetnacl-util

Name:           nodejs-%{npmname}
Version:        0.15.0
Release:        4%{?dist}
Summary:        Some string encoding utilities

License:        Unlicense
URL:            https://www.npmjs.com/package/%{npmname}

# NPM does not include tests.
Source0:        https://github.com/dchest/tweetnacl-util-js/archive/v%{version}/%{npmname}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-tape
BuildRequires:  uglify-js

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
String encoding utilities extracted from early versions of tweetnacl-js.
Used in nodejs-tweetnacl's unit tests.

%prep
%autosetup -n tweetnacl-util-js-%{version}

%build
# We need to uglify some sources. :/
uglifyjs nacl-util.js -c -m -o nacl-util.min.js

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a *.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a *.ts %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
tape test/*.js

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md AUTHORS.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.15.0-1
- Initial package.
