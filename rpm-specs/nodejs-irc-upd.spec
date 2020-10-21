%global npmname irc-upd

Name:           nodejs-%{npmname}
Version:        0.10.0
Release:        6%{?dist}
Summary:        NodeJS IRC client library

License:        GPLv3
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-chardet
BuildRequires:  nodejs-iconv-lite
BuildRequires:  nodejs-irc-colors

BuildRequires:  dos2unix

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
node-irc is an IRC client library written in JavaScript for Node.

%prep
%autosetup -n package

# Convert files from dos2unix and remove executable bits.
dos2unix --force CHANGELOG.md README.md docs/*
chmod -x CHANGELOG.md README.md docs/*

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a lib %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npmname}/
%doc README.md CHANGELOG.md docs/ example/
%license COPYING

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.10.0-2
- Remove spurious executable bits and convert line endings.

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.10.0-1
- Initial package.
