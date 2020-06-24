%define		gem_name		zoom

%if 0%{?fedora} < 19
%define		rubyabi		1.9.1
%endif


Name:		rubygem-%{gem_name}
Version:	0.5.0
Release:	17%{?dist}
Summary:	Ruby binding to ZOOM

License:	LGPLv2+
URL:		http://ruby-zoom.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygem(rake)
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel

BuildRequires:	gcc
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libxslt-devel
BuildRequires:	libyaz-devel

BuildRequires:	rubygem(test-unit)

Requires:	ruby(rubygems)

Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# Obsolete but not provide
# Obsoletes: ruby(zoom) < 0.3.0 does not obsolete ruby-zoom
Obsoletes:	ruby-zoom < 0.3.0

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation 
Model (ZOOM), an abstract object-oriented programming interface 
to a subset of the services specified by the Z39.50 standard, 
also known as the international standard ISO 23950.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


%prep
%setup -q -c -T
TOPDIR=$(pwd)

mkdir TMP
cd TMP

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%{_fixperms} .

gem build %{gem_name}.gemspec
cp -p ./%{gem_name}-%{version}.gem $TOPDIR

%build
%gem_install

chmod 0644 ./%{gem_cache}
find . -type f -print0 | xargs --null chmod ugo+r

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# If there are C extensions, mv them to the extdir.
# $REQUIRE_PATHS is taken from the first value of the require_paths field in
# the gemspec file.  It will typically be either "lib" or "ext".  For instance:
#  s.require_paths = ["lib"] 
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# clean the built bits out
rm -rf %{buildroot}%{gem_instdir}/ext/
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%check
# Net connection needed, disabling now.
#ping -c 3 fedoraproject.org || exit 0
pushd .%{gem_instdir}

ruby \
	-Ilib:.:ext -rzoom -rtest/unit \
	test/*_test.rb

popd

%files
%dir %{gem_extdir_mri}
%{gem_extdir_mri}/*
%dir %{gem_instdir}/
%doc %{gem_instdir}/[A-Z]*

%{gem_spec}

%exclude	%{gem_cache}

%files doc
%{gem_docdir}/
%exclude	%{gem_instdir}/Rakefile
%{gem_instdir}/sample/
%exclude	%{gem_instdir}/test/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-16
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-13
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-11
- Remove unneeded tcp_wrappers-devel BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.5.0-9
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-8
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-4
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-2
- F-24: rebuild against ruby23

* Wed Aug 19 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-1
- 0.5.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.1-24
- F-22: Rebuild for ruby 2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.1-21
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Mon Mar 31 2014 Adam Williamson <awilliam@redhat.com> - 0.4.1-20
- rebuild for new libyaz

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.1-18
- F-19: Rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.1-15
- Fix packaging to really work properly

* Fri Mar 23 2012 Tom Callaway <spot@fedoraproject.org> - 0.4.1-14
- get this thing working

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.1-12
- Fix permission

* Sun Jun 05 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.1-11
- Simplify packaging

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-9
- Add more BRs

* Thu Apr  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-14: rebuild for new yaz

* Sat Sep 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-7
- Fix permission

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-6
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-5
- %%global-ize "nested" macro

* Mon Oct 27 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-4
- Better way to set CFLAGS and create debuginfo rpm correctly

* Wed Oct  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-3
- Split out unneeded files in better way

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Thu Dec  6 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-2.dist.2
- Rebuild against new openssl

* Wed Nov 21 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.1-2
- 0.4.1
- Also update URL

* Tue Nov 13 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.0-1
- 0.3.0, switch to gem.

* Sun Nov  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.3-1
- 0.2.3

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-3.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-3.dist.1
- License update

* Sat Jun 16 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-3
- Rebuild (against new yaz)

* Sat Apr 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-2
- Add more documents

* Sat Apr 21 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.2-1
- Initial packaging
