%global npmname prism-media

Name:           nodejs-%{npmname}
Version:        1.0.1
Release:        4%{?dist}
Summary:        Easily transcode media using node.js

License:        ASL 2.0
URL:            https://www.npmjs.com/package/%{npmname}

# Something is very wrong with the npmjs archive.
Source0:        https://github.com/amishshah/%{npmname}/archive/v%{version}/%{npmname}-%{version}.tar.gz

BuildRequires:  nodejs-packaging

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Intuitive abstractions that make transcoding media easy. Provides
behind-the-scenes audio support for discord.js.

%prep
%autosetup -n %{npmname}-%{version}

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a src/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a typings/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.0.1-1
- Updated to latest upstream release, 1.0.1.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.3.1-1
- Initial package.
