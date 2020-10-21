# spec file for package nodejs-nodejs-columnify

%global npm_name columnify
%{?nodejs_find_provides_and_requires}

%global enable_tests 1
# Tests turned off due to missing dependencies

Name:		nodejs-columnify
Version:	1.5.4
Release:	11%{?dist}
Summary:	Render data in text columns. supports in-column text-wrap
Url:		https://github.com/timoxley/columnify
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# Npm tarball doesn't include tests, so they are pulled by Source10 from github
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-devel
BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
#BuildRequires:	npm(babel)
BuildRequires:	npm(chalk)
#BuildRequires:	npm(tap-spec)
BuildRequires:	npm(tape)
%endif

BuildRequires:	npm(strip-ansi)
BuildRequires:	npm(wcwidth)

%description
Render data in text columns. supports in-column text-wrap

%prep
%setup -q -n package
%setup -T -D -a 1 -q -n package

%{nodejs_fixdep} strip-ansi

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js columnify.js width.js utils.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#make prepublish && tape test/*.js | tap-spec
tape test/*.js
%endif

%files
%{nodejs_sitelib}/columnify

%doc Readme.md
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.5.4-1
- Update to 1.5.4 for npm

* Wed Jun 24 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.1-3
- Switched back to npmjs sources
- added script to pull tests from github

* Sat May 23 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.1-2
- Changed sources to github
- removed scl prefixes

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.1-1
- New upstream release
- removed rm -rf %%buildroot from %%install and %%clean section
- removed unnecessary %%nodejs_fixdep macro
- minor changes

* Thu Mar 19 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.3.2-4
- AddedExclusiveArch, nodejs-packaging dependency, %%nodejs_fixdep macros, %%check and %%license
- removed BuildRoot and %%defattr

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.3.2-3
- New upstream release 1.3.2

* Mon Feb 17 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.2-1
- Initial build 
