# spec file for package nodejs-nodejs-fs-write-stream-atomic

%global npm_name fs-write-stream-atomic
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		nodejs-fs-write-stream-atomic
Version:	1.0.8
Release:	9%{?dist}
Summary:	Like `fs.createWriteStream(...)`, but atomic
Url:		https://github.com/npm/fs-write-stream-atomic
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
BuildRequires:	npm(graceful-fs)
BuildRequires:	npm(iferr)
BuildRequires:	npm(imurmurhash)
BuildRequires:	npm(readable-stream)
BuildRequires:	npm(rimraf)
%endif

%description
Like `fs.createWriteStream(...)`, but atomic


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}
%{nodejs_symlink_deps}


%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%tap test/*.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/fs-write-stream-atomic


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.0.8-1
- Update to 1.0.8 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-1
- New upstream release

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Initial build

