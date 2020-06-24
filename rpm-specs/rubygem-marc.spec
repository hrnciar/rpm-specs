%if 0%{?fedora} >= 17
%if 0%{?fedora} < 19
%global	rubyabi		1.9.1
%endif
%else
%global	rubyabi		1.8
%global	ruby_sitelib            %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%endif

%global		gem_name	marc

Name:		rubygem-%{gem_name}
Version:	1.0.4
Release:	3%{?dist}
Summary:	Ruby library for MARC catalog

License:	MIT
URL:		http://marc.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} >= 19
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby
%endif

BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(xml-simple)
BuildRequires:	rubygem(nokogiri)
BuildRequires:	rubygem(unf)
BuildRequires:	rubygem(ensure_valid_encoding)
BuildRequires:	rubygem(scrub_rb)
%if 0%{?fedora} < 21
Requires:	ruby(rubygems)
Requires:	rubygem(unf)
Requires:	rubygem(ensure_valid_encoding)
Requires:	rubygem(scrub_rb)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
%endif
%if 0%{?fedora} >= 17
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
%endif

BuildArch:	noarch

%description
marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package -n	ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Requires:	%{name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description -n	ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.


%prep
%setup -q -T -c

%gem_install -n %{SOURCE0}

find .%{gem_instdir}/{lib,test} -name \*.rb -print0 | xargs -0 chmod 0644
find .%{gem_instdir}/{lib,test} -name \*.rb -print0 | \
	xargs -0 grep -l --null '#![ \t]*%{_bindir}' | \
	xargs -0 chmod 0755

%build

%install
mkdir -p %{buildroot}%{gem_dir}

cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# specify some UTF-8 locale
LANG=C.UTF-8
ruby -Ilib:. -e 'gem "test-unit"; require "marc" ; Dir.glob("test/tc_*.rb"){|f| require f }'

%files

%dir %{gem_instdir}/
%doc %{gem_instdir}/[A-Z]*
%exclude %{gem_instdir}/Rakefile
%{gem_instdir}/lib/

%{gem_cache}
%{gem_spec}

%files		doc
%{gem_instdir}/Rakefile
%{gem_dir}/doc/%{gem_name}-%{version}/
%{gem_instdir}/test/

%if %{?fedora} < 17
%files -n	ruby-%{gem_name}
%{ruby_sitelib}/%{gem_name}.rb
%{ruby_sitelib}/%{gem_name}/
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-1
- 1.0.4

* Fri Apr  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.2-4
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-1
- 1.0.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb  5 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Wed Dec  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Fri Sep 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-1
- 0.7.1

* Tue Aug 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0-1
- 0.6.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-1
- 0.5.1

* Wed Mar  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-4
- F-19: Rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.5.0-1
- 0.5.0

* Mon Apr  9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.4-1
- 0.4.4

* Sun Feb  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.3-4
- F-17: rebuild against ruby19

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org>
- Rescue test result for now

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.3-1
- 0.4.3

* Thu May  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.2-1
- 0.4.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-1
- 0.4.1

* Fri Sep 24 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.0-1
- 0.4.0

* Sat Dec 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.3-1
- 0.3.3

* Tue Dec 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.1-1
- 0.3.1

* Mon Nov 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.0-2
- Fix Summary
- Surely create .%%{gem_dir} before installing gem file

* Fri Nov 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.0-1
- Switch to gem

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-3
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-2
- %%global-ize "nested" macro

* Thu Jan  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-1
- 0.2.2

* Thu Aug 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.1-1
- 0.2.1

* Thu Jun 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.0-1
- 0.2.0

* Sun Jun  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.9-1
- 0.1.9

* Sun Dec 16 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.8-1
- 0.1.8

* Tue Nov 13 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.7-1
- Initial packaging
