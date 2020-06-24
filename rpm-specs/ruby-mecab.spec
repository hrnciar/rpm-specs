%define		mainver		0.996
#%%define		betaver		pre3
%define		relnumber	6
%define		srcname		mecab-ruby


%if 0%{?fedora} >= 17
%if 0%{?fedora} < 19
%define		rubyver		1.9.1
%endif
%else
%define		rubyver		1.8
%{!?ruby_sitearch:	%global ruby_sitearch	%(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitearchdir"]')}
%{!?ruby_sitelib:	%global ruby_sitelib	%(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')}
%endif

Name:		ruby-mecab
Version:	%{mainver}
Release:	%{?betaver:0.}%{relnumber}%{?betaver:.%betaver}%{?dist}.14
Summary:	Ruby binding for MeCab

# License is the same as MeCab
License:	BSD or LGPLv2+ or GPL+ 
URL:		http://mecab.sourceforge.net/
Source0:	http://mecab.googlecode.com/files/%{srcname}-%{mainver}%{?betaver}.tar.gz

BuildRequires:	gcc-c++
# This is not release number specific
BuildRequires:	mecab-devel = %{version}
# ruby-devel requires ruby-libs and not require ruby
BuildRequires:	ruby
BuildRequires:	ruby-devel
# %%check
BuildRequires:	mecab-jumandic

Requires:	mecab = %{version}
%if 0%{?fedora} >= 19
Requires:	ruby
%else
Requires:	ruby(abi) = %{rubyver}
%endif

Provides:	ruby(mecab) = %{version}-%{release}

%description
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}%{?betaver}

%build
ruby extconf.rb
%{__make} %{?_smp_mflags} \
	CXXFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="%{__install} -c -p" \
%if 0%{?fedora} < 21
	ruby_headers= \
%endif
	RUBYARCHDIR=${RPM_BUILD_ROOT}%{ruby_vendorarchdir}
 
%check
ruby -I. test.rb

%files
%doc bindings.html
%doc AUTHORS COPYING BSD GPL LGPL

%if 0%{?fedora} >= 17
%{ruby_vendorarchdir}/*MeCab*
%else
%{ruby_sitearch}/*MeCab*
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-6.13
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-6.10
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.996-6.7
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-6.6
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-6.2
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-6
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.996-5.1
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-5
- F-22: rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-4
- Revert the previous change, fix conditionals

* Mon Apr 28 2014 Vít Ondruch <vondruch@redhat.com> - 0.996-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-2
- F-19: Rebuild for ruby 2.0.0

* Fri Feb 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-1
- 0.996

* Sun Feb 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.995-1
- 0.995

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.994-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.994-1
- 0.994

* Thu Mar 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.993-1
- 0.993

* Mon Feb  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.991-2
- F-17: rebuild against ruby19

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.991-1
- 0.991

* Mon Jan  9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.99-1
- 0.99

* Mon Feb 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-2
- F-15 mass rebuild

* Tue Sep 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-1
- 0.98

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-0.3.pre3
- F-12: Mass rebuild

* Thu Jun  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-0.2.pre3
- 0.98pre3

* Mon Mar  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-0.1.pre1
- Update to 0.98pre1

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.97-3
- %%global-ize "nested" macro

* Sun Jun  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.97-2
- Remove ancient || : after %%check

* Sun Feb  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.97-1
- 0.97

* Fri Oct 26 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-2
- License fix

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-1.dist.3
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-1.dist.1
- License update

* Mon Jun 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-1
- 0.96 release

* Fri May  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.95-4
- Add license notification text for now.

* Sat Mar 31 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.95-3
- Again change the name to ruby-mecab

* Sat Mar 31 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.95-2
- Build with -fPIC for shared library (#233426)
- Rename to mecab-ruby, drop providing

* Thu Mar 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.95-1
- Initial packaging.
