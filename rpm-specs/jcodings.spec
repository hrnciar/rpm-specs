%global commit_hash d50ee0e
%global tag_hash d50ee0e

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.9
Release:        17%{?dist}
Summary:        Java-based codings helper classes for Joni and JRuby

License:        MIT
URL:            http://github.com/jruby/%{name}
Source0:        https://github.com/jruby/jcodings/tarball/%{version}/jruby-%{name}-%{version}-0-g%{commit_hash}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-source-plugin

%description
Java-based codings helper classes for Joni and JRuby.


%prep
%setup -q -n jruby-%{name}-%{tag_hash}

find -name '*.class' -delete
find -name '*.jar' -delete

%mvn_file : %{name}

%build
echo "See %{url} for more info about the %{name} project." > README.txt

%pom_xpath_remove "pom:build/pom:extensions"
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0.9-10
- Add missing BuildRequires to fix FTBFS (BZ#1406099).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.9-6
- Use Requires: java-headless rebuild (#1067528)

* Thu Aug 29 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0.9-5
- Fix unowned dir.

* Thu Aug 29 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0.9-4
- Update for latest guidelines, rhbz #992612

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.9-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 25 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.9-1
- Updated to version 1.0.9.
- Switch to maven builds, as it seems to be preffered upstream way.

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 1.0.5-4
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.5-1
- update to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 09 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.2-2
- Fix the clean up code in the prep section
- Fix typo
- Save changelog

* Thu Jan 28 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.2-1
- 1.0.2
- Remove gcj bits
- New URL
- Update summary and description
- Use macros in all sections of the spec
- Add README.txt generated on the fly

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.1-1
- Bump to 1.0.1 for jruby 1.1.6.

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 1.0-2
- Add gcj bits.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 1.0-1
- Initial package (needed for jruby 1.1.5 and joni 1.1.1).
