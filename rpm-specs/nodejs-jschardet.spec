%{?nodejs_find_provides_and_requires}

%global packagename jschardet
%global enable_tests 0
# tests disabled until dev dependencies are available

Name:		nodejs-jschardet
Version:	1.4.2
Release:	8%{?dist}
Summary:	Character encoding auto-detection in JavaScript (port of python's chardet)

License:	LGPLv2+
# License is at the top of src/init.js, but we'll split it out into a separate file in prep
URL:		https://github.com/aadsm/jschardet.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(qunit)
%endif

%description
Character encoding auto-detection in JavaScript (port of python's chardet)


%prep
%setup -q -n package
# License is at the top of src/init.js, but we'll split it out into a separate file now
head -n 30 src/init.js > LICENSE-LGPL.txt

# Remove bundled version of qunit
rm -rf tests/qunit/

# Add shebang
sed -i '1s;^;#!/usr/bin/node\n;' *.js

# remove executable bits from files that don't need them
chmod -x README.md package.json src/*.js

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js src/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/qunit -c jschardet:src/init.js -t tests/jschardet.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-LGPL.txt
%{nodejs_sitelib}/%{packagename}



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Jared Smith <jsmith@fedoraproject.org> - 1.4.2-1
- Update to upstream 1.4.2 release

* Mon Nov 30 2015 Jared Smith <jsmith@fedoraproject.org> - 1.4.1-1
- Initial packaging
