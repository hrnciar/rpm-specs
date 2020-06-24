%global commit 0a3b42373f38883cc1f68388eba33967baac8980
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           jabrt
Version:        1.0
Release:        11.git%{shortcommit}%{?dist}
Summary:        ABRT Java bindings

License:        GPLv2+
URL:            https://github.com/mozeq/%{name}
Source0:        http://jmoskovc.fedorapeople.org/jabrt-1.0-git%{shortcommit}.tar.gz
Source1:        http://www.gnu.org/licenses/gpl-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(junit:junit)


%description
ABRT Java bindings providing a convenient way to report problems

%package javadoc
Summary: API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{version}-%{commit}

cp %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2.git0a3b423
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep  6 2013 Jiri Moskovcak <jmoskovc@redhat.com> 1.0-1.git0a3b423
- initial packaging
