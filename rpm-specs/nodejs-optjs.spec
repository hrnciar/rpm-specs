%{?nodejs_find_provides_and_requires}

%global packagename optjs
%global enable_tests 1

Name:		nodejs-optjs
Version:	3.2.2
Release:	8%{?dist}
Summary:	Probably the sole command line option parser you'll ever need

License:	MIT
URL:		https://github.com/dcodeIO/opt.js
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# License requested at https://github.com/dcodeIO/opt.js/issues/1
Source1:	LICENSE-MIT.txt


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
# nothing
%endif

%description
Probably the sole command line option parser you'll ever need to...


%prep
%setup -q -n package
# setup the license file
cp -p %{SOURCE1} .



%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json opt.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} test.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-MIT.txt
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Jared Smith <jsmith@fedoraproject.org> - 3.2.2-1
- Update to upstream 3.2.2 release
- Changle license to reflect upstream change to MIT license

* Mon Nov 16 2015 Jared Smith <jsmith@fedoraproject.org> - 3.2.1-1
- Initial packaging
