# spec file for package nodejs-nodejs-write-file-atomic

%global npm_name write-file-atomic
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		nodejs-write-file-atomic
Version:	1.1.4
Release:	9%{?dist}
Summary:	Write files in an atomic fashion w/configurable ownership
Url:		https://github.com/iarna/write-file-atomic
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
BuildRequires:	npm(graceful-fs)
BuildRequires:	npm(imurmurhash)
BuildRequires:	npm(require-inject)
BuildRequires:	npm(slide)
%endif

%description
Write files in an atomic fashion w/configurable ownership


%prep
%setup -q -n package
rm -rf node_modules


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%tap test/*.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/write-file-atomic


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 1.1.4-1
- Update to 1.1.4 upstream release
- Enable tests

* Sat May 23 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-2
- Added %%nodejs_fixdep macro

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-1
- Rebuilt with new upstream release
- minor changes

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-1
- Initial build
