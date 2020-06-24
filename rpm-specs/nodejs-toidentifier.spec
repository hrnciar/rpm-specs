%global npmname toidentifier

Name:           nodejs-%{npmname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Convert a string of words to a JavaScript identifier

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://github.com/component/%{npmname}/archive/v%{version}/%{npmname}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs

# mocha is used to run the tests.
BuildRequires:  mocha

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Convert a string of words to a JavaScript identifier.

%prep
%autosetup -n %{npmname}-%{version}

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} --experimental-modules -e 'require("./")'
mocha --reporter spec --bail --check-leaks test/

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md

%changelog
* Tue Feb 18 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.0.0-1
- Initial package for Fedora.
