%if 0%{?fedora} < 19
%define		rubyabi		1.9.1
%endif

Name:		ruby-bsearch
Version:	1.5
Release:	21%{?dist}
Summary:	Binary search library for Ruby
License:	Ruby
URL:		http://0xcc.net/ruby-bsearch/
Source0:	http://0xcc.net/ruby-bsearch/%{name}-%{version}.tar.gz

# make it sure that the ruby used for build has
# the same abi as which is used at runtime
%if 0%{?fedora} >= 19
BuildRequires:	ruby(release)
Requires:	ruby(release)
%else
BuildRequires:	ruby(abi) = %{rubyabi}
Requires:	ruby(abi) = %{rubyabi}
%endif
BuildRequires:	ruby
BuildRequires:	ruby-devel
Provides:	ruby(bsearch) = %{version}-%{release}
BuildArch:	noarch

%description
Ruby/Bsearch is a binary search library for Ruby. It can search the FIRST or
LAST occurrence in an array with a condition given by a block.

%prep
%setup -q

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{ruby_vendorlibdir}
%{__install} -c -p -m 644 bsearch.rb $RPM_BUILD_ROOT%{ruby_vendorlibdir}/

%check
cd tests ; sh test.sh
cd ..

%files
%doc ChangeLog bsearch.en.rd
%doc bsearch.png
%lang(ja) %doc bsearch.ja.rd
%{ruby_vendorlibdir}/bsearch.rb


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-10
- F-19: rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-3
- %%global-ize "nested" macro

* Thu Apr  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-2
- Fix URL (thanks to Kevin Fenzi)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-1.dist.1
- License update

* Thu Apr 12 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-1
- Rewrite

* Sun Apr 08 2007 Minokichi Sato <m-sato@rc.kyushu-u.ac.jp>
- First build for Fedora Core 6
