# See https://fedoraproject.org/wiki/Packaging:Node.js?rd=Node.js/Packagers for
# the nodejs-specific packaging guidelines.

# See https://fedoraproject.org/wiki/Packaging:Node.js?rd=Node.js/Packagers#Automatic_Requires_and_Provides
# (required for EPEL compatibility)
%{?nodejs_find_provides_and_requires}

%global npm_name xdg-basedir

Name:		nodejs-xdg-basedir
Version:	4.0.0
Release:	3%{?dist}
Summary:	A JavaScript library to work with XDG Base Directory paths

License:	MIT
URL:		https://github.com/sindresorhus/xdg-basedir
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch
BuildRequires:	nodejs-packaging

%description
%{summary}.

%prep
%setup -q -n package

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%check
%{__nodejs} -e 'require("./")'

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Timothée Floure <fnux@fedoraproject.org> - 4.0.0-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jan 18 2018 Timothée Floure <fnux@fedoraproject.org> - 3.0.0-2
- Remove the deprecated 'Group' tag
- Add a check section to comply with the packaging guidelines

* Mon Jun 26 2017 Timothée Floure <fnux@fnux.ch> - 3.0.0-1
- Let there be package
