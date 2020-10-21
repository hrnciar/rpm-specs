%{?scl:%scl_package nodejs-github-url-from-username-repo}
%{!?scl:%global pkg_name %{name}}

%global npm_name github-url-from-username-repo

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		%{?scl_prefix}nodejs-github-url-from-username-repo
Version:	1.0.2
Release:	13%{?dist}
Summary:	Create urls from username/repo
Url:		https://github.com/robertkowalski/github-url-from-username-repo
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	BSD
BuildRequires:	nodejs-packaging
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

%if 0%{?enable_tests}
BuildRequires:	npm(mocha)
%endif

%description
Create urls from username/repo

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{nodejs_sitelib}/github-url-from-username-repo
cp -pr index.js package.json %{buildroot}/%{nodejs_sitelib}/github-url-from-username-repo

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check --no-devdeps
mocha -R spec
%endif

%files
%{nodejs_sitelib}/github-url-from-username-repo
%doc README.md
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 12 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-3
- Removed dependency

* Wed Apr 15 2015 Zuzana Svetlikova - 1.0.2-1
- New upstream release 1.0.2
- corrected license

* Mon Mar 16 2015 Zuzana Svetlikova - 1.0.0-2
- Removed %%defattr
- added nodejs_symlink_deps macro, %%license, nodejs-packaging dependency and ExclusiveArch
- finished %%check

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- New upstream release 1.0.0

* Thu Jan 23 2014 Tomas Hrcka <thrcka@redhat.com> - 0.0.2-1
- Package import
