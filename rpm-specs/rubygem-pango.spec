%global	header_dir	%{ruby_vendorarchdir}


%global	gem_name	pango
%global	gem_name_gi pango
%global	gem_name_no_gi pango-no-gi

%global	glibminver	3.1.3
%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of pango-1.x
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	1%{?dist}
# from README
License:	LGPLv2
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# no-gi version
Source1:	pango-no-gi-%{version}.tar.gz
# Source1 is created from Source2
Source2:	pango-create-no-gi-src.sh
# Backport rbpango_attribute_{to,from}_ruby definition
Patch10:	pango-no-gi-3.3.7-backport-def.patch

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	gcc

BuildRequires:	rubygems-devel
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem(cairo-gobject)
BuildRequires:	rubygem-gobject-introspection-devel
BuildRequires:	ruby-devel
BuildRequires:	pango-devel
# %%check
BuildRequires:	rubygem(test-unit)
# One mono font (test_load_font)
BuildRequires:	liberation-mono-fonts
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}

Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/Pango is a Ruby binding of pango-1.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

# Create no-gi for now
%package	-n rubygem-%{gem_name_no_gi}
Summary:	Ruby binding of pango-1.x with no-gi version
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(mechanize)
# For now, explicitly
Requires:	rubygem(glib2)
Requires:	rubygem(cairo)
Provides:	rubygem(pango-no-gi) = %{version}-%{release}

%description -n rubygem-%{gem_name_no_gi}
Ruby/Pango is a Ruby binding of pango-1.x.
This package contains no-gi implementation of Ruby/Pango.

%package	-n rubygem-%{gem_name_no_gi}-doc
Summary:	Documentation for %{name} no-gi
Requires:	rubygem-%{gem_name_no_gi} = %{version}-%{release}

%description	-n rubygem-%{gem_name_no_gi}-doc
This package contains documentation for ubygem-%{gem_name_no_gi}.

%package	devel
Summary:	Ruby/pango development environment
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-devel
Requires:	pango-devel
Requires:	rubygem-cairo-devel
# Obsoletes / Provides
# ruby(%%{gem_name}-devel) Provides is for compatibility
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}.gemspec

# Fix wrong shebang

# Kill shebang

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}.gemspec
%gem_install

######
# Create no-gi for now
rm -rf no-gi
mkdir no-gi
pushd no-gi

tar xf %{SOURCE1}
chmod ugo+rX .
pushd pango-no-gi
cat %PATCH10 | patch -p1
mv ext/pango ext/pango-no-gi
rake gem
popd

cp -a pango-no-gi/pkg/%{gem_name_no_gi}-%{version}.gem .

# Change for now
%global gem_name %gem_name_no_gi
gem unpack %{gem_name}-%{version}.gem
pushd %{gem_name}-%{version}

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
        xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

gem spec ../%{gem_name}-%{version}.gem -l --ruby > %{gem_name}.gemspec
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}.gemspec
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem ..
popd

%gem_install -n ./%{gem_name}-%{version}.gem
chmod -R ugo+rX .

# Back
%global gem_name %gem_name_gi
popd

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/

# Cleanups
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd

### For no-gi
%global gem_name %gem_name_no_gi

pushd no-gi
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
# mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f ./%{gem_extdir_mri}/*.h
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# Cleanups
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -rf .%{gem_instdir}/test/
rm -f .%{gem_instdir}/Rakefile
rm -f .%{gem_instdir}/extconf.rb
popd
popd

%global gem_name %gem_name_gi


%check
pushd .%{gem_instdir}

# kill unneeded make process
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd

# test_default(TestLanguage) [./test/test-language.rb] needs LANG=ja_JP.UTF-8, for example
LANG=C.UTF-8
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
# Ignore floating point difference on i686 for now
ruby -Ilib:test:ext/%{gem_name} ./test/run-test.rb \
%ifarch %ix86
	'--ignore-name=/test_rotate!*/' \
%endif
	%{nil}

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_instdir}/*gemspec

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_instdir}/lib/%{gem_name}/
%{gem_extdir_mri}

%exclude	%{gem_cache}
%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc
%{header_dir}/rb-pango.h
%{header_dir}/rb-pango-conversions.h

%files	doc
%{gem_dir}/doc/%{gem_name}-%{version}
%exclude	%{gem_instdir}/Rakefile
%{gem_instdir}/test/

# Again:
%global gem_name %gem_name_no_gi
%files	-n rubygem-%{gem_name_no_gi}
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%doc	%{gem_instdir}/[A-Z]*

# The following should be "pango.rb"
%{gem_instdir}/lib/pango.rb
%{gem_extdir_mri}
%exclude	%{gem_cache}
%{gem_spec}

%files	-n rubygem-%{gem_name_no_gi}-doc
%{gem_docdir}
%{gem_instdir}/sample/

%global gem_name %gem_name_gi


%changelog
* Thu Aug 13 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-1
- 3.4.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-2
- F-32: rebuild against ruby27

* Wed Dec  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Sat Oct 12 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Thu Oct  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.8-1
- 3.3.8

* Sun Sep  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-2
- Rebuild again

* Fri Sep  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Sun Feb 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-3
- F-30: rebuild against ruby26

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.0-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Wed Nov 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-1
- 3.2.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-2
- Backport rbpango_attribute_{to,from}_ruby def to no-gi

* Wed Jun 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Wed Apr 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.1-3
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-2
- F-28: rebuild for ruby25

* Tue Nov 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Sat Oct 21 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Wed Jul 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Fri Jun  9 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-3
- Fix shebang for -no-gi-doc

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-2
- no-gi: add vitrual provides

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6
- Create no-gi for now

* Thu May  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Thu May  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-3
- Once relax dependency

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-2
- F-26: rebuild for ruby24

* Tue Nov 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Tue Sep 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-3
- Fix misterious Obsoletes

* Sat Aug 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-2
- Add one monospace font as BR for test suite
  (test_load_font)

* Sun Aug 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Tue Apr 19 2016 TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-2
- F-24: rebuild against ruby23

* Sun Oct 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Wed Sep 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Tue Sep 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.4-1
- 3.0.4

* Sun Sep 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-1
- 2.2.5

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-2
- F-22: Rebuild for ruby 2.2

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-1
- 2.2.4

* Wed Nov  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-1
- 2.2.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-2
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Fri Apr 11 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Thu Jan 16 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1
- 2.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-1
- 1.2.6

* Thu Apr  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-1
- 1.2.5

* Tue Mar 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-1
- 1.2.4

* Wed Mar 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Sun Mar  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-2
- F-19: Rebuild for ruby 2.0.0

* Mon Feb  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Wed Jan 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Mon Dec 31 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.9-1
- 1.1.9

* Thu Dec  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Wed Sep  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.5-1
- 1.1.5

* Mon Aug 13 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.4-1
- 1.1.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.2-4
- Fix conditionals for F17 to work for RHEL 7 as well.

* Wed Feb  1 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-4
- Add proper Obsoletes/Provides

* Tue Jan 31 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.2-3
- 1.1.2

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Fri Jul 15 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Sun Jun 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.9-1
- 0.90.9

* Sat Mar  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.90.8-1
- 0.90.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.7-2
- 0.90.7

* Sun Oct 31 2010 Mamoru Taska  <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.5-2
- 0.90.5
- Move C extension so that "require %%gem_name" works correctly

* Sun Oct 24 2010 Mamoru Taska  <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.4-2
- 0.90.4

* Sun Oct 24 2010 Mamoru Taska  <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.3-2
- 0.90.3

* Fri Oct  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-5
- Fix up summary
- Fix Requires for -devel subpackage

* Fri Oct  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-4
- Use formally released gem file

* Tue Sep 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.2-2
- Initial package
