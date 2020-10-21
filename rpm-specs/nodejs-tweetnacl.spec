%global npmname tweetnacl

Name:           nodejs-%{npmname}
Version:        1.0.1
Release:        5%{?dist}
Summary:        Port of TweetNaCl cryptographic library to JavaScript

License:        Unlicense
URL:            https://www.npmjs.com/package/%{npmname}

# NPM does not include tests.
Source0:        https://github.com/dchest/tweetnacl-js/archive/v%{version}/%{npmname}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-tape
BuildRequires:  nodejs-tweetnacl-util
BuildRequires:  uglify-js

# Some of the tests are written in C.
BuildRequires:  gcc

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
The primary goal of this project is to produce a translation of TweetNaCl
to JavaScript which is as close as possible to the original C
implementation, plus a thin layer of idiomatic high-level API on top of it.

There are two versions, you can use either of them:

nacl.js is the port of TweetNaCl with minimum differences from the original
+ high-level API.

nacl-fast.js is like nacl.js, but with some functions replaced with faster
versions. (Used by default when importing NPM package.)

%prep
%autosetup -n tweetnacl-js-%{version}

%build
# We need to uglify some sources. :/
uglifyjs nacl.js -c -m -o nacl.min.js
uglifyjs nacl-fast.js -c -m -o nacl-fast.min.js

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a *.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a *.ts %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
make -C test/c
tape test/*.js test/c/*.js

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md AUTHORS.md CHANGELOG.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.0.1-1
- Updated to latest upstream release (rhbz#1669193).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.0.0-1
- Initial package.
