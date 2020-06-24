# spec file for package nodejs-nodejs-fs-vacuum

%global npm_name fs-vacuum
%{?nodejs_find_provides_and_requires}

Name:		nodejs-fs-vacuum
Version:	1.2.7
Release:	9%{?dist}
Summary:	Recursively remove empty directories -- to a point
Url:		https://github.com/npm/fs-vacuum
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

BuildRequires:	npm(tap)
BuildRequires:	npm(graceful-fs)
BuildRequires:	npm(mkdirp)
BuildRequires:	npm(path-is-inside)
BuildRequires:	npm(rimraf)
BuildRequires:	npm(tmp)

%description
Recursively remove empty directories -- to a point


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json vacuum.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}
%{nodejs_symlink_deps}


%check
%{nodejs_symlink_deps} --check
%tap test/*.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/fs-vacuum


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.2.7-1
- Update to 1.2.7 upstream release
- Enable tests

* Tue Jul 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.6-2
- Added %%nodejs_fixdep macros

* Mon Jul 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.6-1
- New upstream release
- updated spec file
- added %%license

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com>- 1.2.5-1
- Initial build
