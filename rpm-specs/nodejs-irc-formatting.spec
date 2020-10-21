%global npmname irc-formatting

# It looks like irc-formatting was never actually released.
%global rctag rc3

Name:           nodejs-%{npmname}
Version:        1.0.0
Release:        0.5.%{rctag}%{?dist}
Summary:        Turns IRC formatted text into easy to use blocks

License:        ISC
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}-%{rctag}.tgz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-zeropad

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Turns IRC formatted text into easy to use blocks. This library is meant to
parse and facilitate compiling to and from the irc caret notation.

%prep
%autosetup -n package

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a lib %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
# No LICENSE in package.
# Upstream seems to have vanished; npm does not have a source repository.
# License text is at the bottom of the README.
%{nodejs_sitelib}/%{npmname}/
%doc readme.md

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.4.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.0.0-0.1.rc3
- Initial package.
