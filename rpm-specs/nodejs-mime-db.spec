%{?nodejs_find_provides_and_requires}

%global packagename mime-db
%global enable_tests 1

Name:		nodejs-mime-db
Version:	1.26.0
Release:	10%{?dist}
Summary:	This is a database of all mime types

License:	MIT
URL:		https://github.com/jshttp/mime-db
Source0:	https://github.com/jshttp/mime-db/archive/v%{version}.tar.gz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

Requires:	nodejs

%description
This is a database of all mime types. It consists of a single, public JSON
file and does not include any logic, allowing it to remain as un-opinionated
as possible with an API. It aggregates data from the following sources:

 * http://www.iana.org/assignments/media-types/media-types.xhtml
 * http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types
 * http://hg.nginx.org/nginx/raw-file/default/conf/mime.types


%prep
%setup -q -n %{packagename}-%{version}


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js db.json src/ scripts/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/mocha -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.26.0-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Jared Smith <jsmith@fedoraproject.org> - 1.26.0-1
- Update to upstream 1.26.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 1.22.0-1
- Update to upstream 1.22.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Jared Smith <jsmith@fedoraproject.org> - 1.21.0-1
- Update to upstream 1.21.0 release

* Fri Nov 13 2015 Jared Smith <jsmith@fedoraproject.org> - 1.20.0-1
- Update to upstream 1.20.0 release

* Thu Oct 22 2015 Jared Smith <jsmith@fedoraproject.org> - 1.19.0-2
- Fix %%license macro for EPEL6

* Wed Oct  7 2015 Jared Smith <jsmith@fedoraproject.org> - 1.19.0-1
- Initial packaging
