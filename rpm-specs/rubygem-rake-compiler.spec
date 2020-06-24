%global	gemname	rake-compiler
%global	gem_name	%{gemname}
%global	gemdir		%{gem_dir}
%global	geminstdir	%{gem_instdir}

%global	rubyabi	1.8

%if %{?fedora:0%{fedora} >= 17}%{?rhel:0%{rhel} >= 7}
%global	gemdir	%{gem_dir}
%global	gem_name	%{gemname}
%global	geminstdir	%{gem_instdir}
%if 0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif
%global	ruby19	1
%else
%global	ruby19	0
%endif

%undefine       _changelog_trimtime

Summary:	Rake-based Ruby C Extension task generator
Name:		rubygem-%{gemname}
Version:	1.1.0
Release:	2%{?dist}
License:	MIT
URL:		http://rake-compiler.rubyforge.org/
Source0:	https://rubygems.org/gems/%{gemname}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	ruby(rubygems) >= 1.3.5
#BuildRequires:	rubygem(cucumber)
#BuildRequires:	rubygem(isolate)
BuildRequires:	rubygem(rake)
#BuildRequires:	rubygem(rcov)
BuildRequires:	rubygem(rspec) >= 3
BuildRequires:	rubygems-devel
Requires:	ruby(rubygems) >= 1.3.5
Requires:	rubygem(rake) >= 0.8.3
BuildArch:	noarch
Provides:	rubygem(%{gemname}) = %{version}-%{release}

%description
rake-compiler aims to help Gem developers while dealing with
Ruby C extensions, simplifiying the code and reducing the duplication.

It follows *convention over configuration* and set an standarized
structure to build and package C extensions in your gems.

This is the result of expriences dealing with several Gems 
that required native extensions across platforms and different 
user configurations where details like portability and 
clarity of code were lacking. 

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# rpmlint cosmetic
find ./lib/rake -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gemdir}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

%check
pushd .%{geminstdir}
ruby -Ilib -S rspec spec/
popd

%files
%{_bindir}/rake-compiler

%dir %{geminstdir}
%doc %{geminstdir}/README.md
%doc %{geminstdir}/LICENSE.txt
%doc %{geminstdir}/History.txt
%{geminstdir}/cucumber.yml
%exclude	%{geminstdir}/appveyor.yml

%{geminstdir}/bin/
%{geminstdir}/features/
%{geminstdir}/lib/
%{geminstdir}/tasks/

%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%{gemdir}/doc/%{gemname}-%{version}
%exclude	%{geminstdir}/Gemfile
%exclude	%{geminstdir}/Rakefile
%{geminstdir}/spec/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Tue Dec 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.9-1
- 1.0.9

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-1
- 1.0.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.7-2
- Rebuild

* Thu Jan 10 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.7-1
- 1.0.7

* Sun Dec 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-1
- 1.0.6

* Thu Dec 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-2
- rebuild

* Wed Sep  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-1
- 1.0.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-1
- 1.0.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Sun Jun 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Sun May 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.9-1
- 0.9.9

* Wed May  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.8-2
- 0.9.8

* Wed Mar 23 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.7-1
- 0.9.7

* Wed Mar  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-1
- 0.9.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5-1
- 0.9.5

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.4-1
- 0.9.4

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-1
- 0.9.3

* Thu Jun 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-3
- Adjust test suite for ruby 2.1.x

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2

* Thu Aug  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1-1
- 0.9.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-3
- Fix test failure with ruby200

* Fri Feb 22 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.3-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-1
- 0.8.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-2
- Fix BR

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.0-2
- Rebuild against ruby 1.9

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.0-1
- 0.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.9-2
- Kill BR: rubygem(rcov) for now

* Sat Jun 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.9-1
- 0.7.9
- %%check now uses rspec, not spec

* Sat Apr 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.8-1
- 0.7.8

* Mon Apr  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.7-1
- 0.7.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.6-1
- 0.7.6

* Tue Nov 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.5-2
- 0.7.5
- Move more files to -doc
- Now needs rubygem(isolate) and some other rubygem(foo) for BR

* Wed Aug 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- 0.7.1

* Thu Dec 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.0-1
- 0.7.0

* Wed Jul 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0-1
- 0.6.0

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-2
- F-12: Mass rebuild

* Thu Jul  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-2
- Restore files under %%{geminstdir}/bin

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-1
- Initial package