%{?nodejs_find_provides_and_requires}

%global packagename mv
%global enable_tests 1

Name:		nodejs-mv
Version:	2.1.1
Release:	9%{?dist}
Summary:	A fs.rename that works across devices. Same as the unix utility 'mv'

License:	MIT
URL:		https://github.com/andrewrk/node-mv.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(ncp)
BuildRequires:	npm(rimraf)
%endif

Requires:	nodejs

%description
A fs.rename that works across devices. Same as the unix utility 'mv'


%prep
%setup -q -n package

%nodejs_fixdep rimraf ^2.6

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 05 2017 Jared Smith <jsmith@fedoraproject.org> - 2.1.1-3
- Relax version on npm(rimraf) a bit more

* Mon Jan 16 2017 Jared Smith <jsmith@fedoraproject.org> - 2.1.1-2
- Relax dependency on npm(rimraf)

* Fri Nov  6 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.1-1
- Initial packaging
