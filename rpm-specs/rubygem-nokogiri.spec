%global	mainver		1.10.10
#%%global	prever		.rc3

%global	mainrel		1
%global	prerpmver		%(echo "%{?prever}" | sed -e 's|\\.||g')

%global	gem_name	nokogiri

%undefine __brp_mangle_shebangs
%undefine	_changelog_trimtime

Summary:	An HTML, XML, SAX, and Reader parser
Name:		rubygem-%{gem_name}
Version:	%{mainver}
Release:	%{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}%{?dist}
License:	MIT
URL:		http://nokogiri.rubyforge.org/nokogiri/
Source0:	https://rubygems.org/gems/%{gem_name}-%{mainver}%{?prever}.gem
# %%{SOURCE2} %%{name} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:	nokogiri-create-full-tarball.sh
# ./test/html/test_element_description.rb:62 fails, as usual......
# Patch0:		rubygem-nokogiri-1.5.0.beta3-test-failure.patch
#Patch0:		rubygem-nokogiri-1.5.0-allow-non-crosscompile.patch
# Shut down libxml2 version unmatching warning
Patch0:	%{name}-1.6.6.4-shutdown-libxml2-warning.patch
BuildRequires:	ruby(release)
BuildRequires:	ruby(rubygems)
##
## For %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygems-devel
Obsoletes:		ruby-%{gem_name} <= 1.5.2-2
#BuildRequires:	ruby(racc)
##
## Others
BuildRequires:	gcc
BuildRequires:	rubygem(pkg-config)
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	ruby-devel
# ruby27 needs this explicitly
BuildRequires:	rubygem(racc)
Requires:	rubygem(racc)

%description
Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath support.

Nokogiri also features an Hpricot compatibility layer to help ease the change
to using correct CSS and XPath.

%if 0
%package	jruby
Summary:	JRuby support for %{name}
Requires:	%{name} = %{version}-%{release}

%description	jruby
This package contains JRuby support for %{name}.
%endif


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	-n ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Requires:	%{name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description	-n ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%global	version	%{mainver}%{?prever}

%prep
%setup -q -T -c -a 1

# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# patches
%patch0 -p1

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec

# remove bundled external libraries
sed -i \
	-e 's|, "ports/archives/[^"][^"]*"||g' \
	-e 's|, "ports/patches/[^"][^"]*"||g' \
	%{gem_name}.gemspec
# Actually not needed when using system libraries
sed -i -e '\@mini_portile@d' %{gem_name}.gemspec

# Ummm...
LANG=C.UTF-8 gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p ./%{gem_dir}
# 1.6.0 needs this
export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

%gem_install


# Permission
chmod 0644 .%{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem

# Remove precompiled Java .jar file
rm -f .%{gem_instdir}/lib/*.jar
# For now remove JRuby support
rm -rf .%{gem_instdir}/ext/java


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

# Remove backup file
find %{buildroot} -name \*.orig_\* | xargs rm -vf

# move arch dependent files to %%gem_extdir
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd


# move bin/ files
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

# remove all shebang
for f in $(find %{buildroot}%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

# Copy document files from full source
cp -p %{gem_name}-%{version}/[A-Z]* %{buildroot}%{gem_instdir}/

# cleanups
rm -rf %{buildroot}%{gem_instdir}/ext/%{gem_name}/
rm -rf %{buildroot}%{gem_instdir}/tmp/
rm -f %{buildroot}%{gem_instdir}/{.autotest,.require_paths,.gemtest,.travis.yml}
rm -f %{buildroot}%{gem_instdir}/appveyor.yml
rm -f %{buildroot}%{gem_instdir}/.cross_rubies
rm -f %{buildroot}%{gem_instdir}/{build_all,dependencies.yml,test_all}
rm -f %{buildroot}%{gem_instdir}/.editorconfig
rm -rf %{buildroot}%{gem_instdir}/suppressions/
rm -rf %{buildroot}%{gem_instdir}/patches/
rm -f %{buildroot}%{gem_instdir}/{Rakefile,Gemfile*}
rm -f %{buildroot}%{gem_instdir}/Manifest.txt



%check
# Ah....
# test_exslt(TestXsltTransforms) [./test/test_xslt_transforms.rb:93]
# fails without TZ on sparc
export TZ="Asia/Tokyo"
#???
LANG=C.UTF-8

# Copy test files from full tarball
cp -a %{gem_name}-%{version}/test/ ./%{gem_instdir}
pushd ./%{gem_instdir}

# Remove unneeded simplecov coverage test
sed -i test/helper.rb \
	-e '\@require.*simplecov@,\@^end$@d'

# Need investigation. For now anyway build
ruby \
	-I.:lib:test:ext \
	-e \
	"require 'test/helper' ; Dir.glob('test/**/test_*.rb'){|f| require f}" || \
	exit 1
	echo "Please investigate this"

for f in $SKIPTEST
do
	mv $f.skip $f
done

popd

%files
%defattr(-,root, root,-)
%{_bindir}/%{gem_name}
%{gem_extdir_mri}/

%dir	%{gem_instdir}/
%doc	%{gem_instdir}/[A-Z]*

%{gem_instdir}/bin/
%{gem_instdir}/lib/
%exclude	%{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem
%{gem_dir}/specifications/%{gem_name}-%{mainver}%{?prever}.gemspec

%if 0
%files	jruby
%defattr(-,root,root,-)
%{gem_instdir}/ext/java/
%endif

%files	doc
%defattr(-,root,root,-)
#%%{gem_instdir}/deps.rip
#%%{gem_instdir}/spec/
%exclude %{gem_instdir}/tasks/
%exclude %{gem_instdir}/test/
%{gem_dir}/doc/%{gem_name}-%{mainver}%{?prever}/

%changelog
* Sat Aug  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.10-1
- 1.10.10

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar  6 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.9-1
- 1.10.9

* Thu Feb 13 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.8-1
- 1.10.8

* Fri Jan 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.7-3
- Also Requires rubygem(racc)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.7-2
- F-32: rebuild against ruby27

* Fri Dec  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.7-1
- 1.10.7

* Tue Nov  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.5-1
- 1.10.5

* Fri Aug 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.4-1
- 1.10.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.3-1
- 1.10.3

* Tue Mar 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.2-1
- 1.10.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.1-1
- 1.10.1

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.0-2
- F-30: rebuild against ruby26

* Wed Jan  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.0-1
- 1.10.0

* Mon Dec 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.1-1
- 1.9.1

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.5-1.1
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Oct  9 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.5-1
- 1.8.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.4-1
- 1.8.4

* Mon Jun 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.3-1
- 1.8.3

* Tue Feb  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.2-1
- 1.8.2

* Thu Jan 25 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.1-1.3
- Drop compatibility with old releases

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.8.1-1.2
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.1-1.1
- F-28: rebuild for ruby25

* Wed Sep 20 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.1-1
- 1.8.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.0-1
- 1.8.0

* Fri May 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-1
- 1.7.2

* Tue Mar 21 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.1-1
- 1.7.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.0.1-2
- F-26: rebuild for ruby24

* Thu Jan  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.0.1-1
- 1.7.0.1

* Thu Dec 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.0-1
- 1.7.0

* Mon Oct 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.8.1-1
- 1.6.8.1

* Fri Jul  1 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.8-3
- Kill pkg-config runtime redundant dependency (bug 1349893)

* Mon Jun 20 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.8-2
- 1.6.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.7.2-1
- 1.6.7.2

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.7-0.4.rc4
- F-24: rebuild against ruby23

* Fri Dec 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.7-0.3.rc3
- Shutdown libxml2 version mismatch warning

* Tue Dec  8 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.7-0.2.rc3
- Rebuild against new libxml2, to make rspec test succeed

* Thu Sep 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.7-0.1.rc3
- 1.6.7.rc3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.6.2-1
- 1.6.6.2

* Fri Jan 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.6.1-1
- 1.6.6.1

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.5-2
- Rebuild for ruby 2.2

* Mon Dec  1 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.5-1
- 1.6.5

* Fri Nov  7 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.4.1-1
- 1.6.4.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.3.1-1
- 1.6.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.2.1-1
- 1.6.2.1

* Thu Apr 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.1-2
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Wed Dec 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.1-1
- 1.6.1

* Fri Oct  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.0-1
- 1.6.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.9-1
- 1.5.9

* Tue Mar 26 2013 Vít Ondruch <vondruch@redhat.com> - 1.5.6-3
- Use %%{gem_extdir_mri} instead of %%{gem_extdir}.

* Sat Feb 23 2013 Vít Ondruch <vondruch@redhat.com> - 1.5.6-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.6-1
- A Happy New Year
- 1.5.6

* Fri Aug 17 2012 Vít Ondruch <vondruch@redhat.com> - 1.5.5-2
- Rebuilt againts libxml2 2.9.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.5-1
- 1.5.5

* Mon May 28 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.2-3
- Fix Obsoletes (bug 822931)

* Mon Apr  9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.2-1
- 1.5.2

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.0-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Tue Jan 24 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-2
- F-17: rebuild for ruby19
- For now aviod build failure by touching some files

* Thu Jan 18 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-1
- 1.5.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.5.beta4.1
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-0.5.beta4
- Remove unneeded patch

* Thu Mar 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-0.4.beta4
- Patch for newer rake to make testsuite run

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.3.beta4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.3.beta4
- 1.5.0.beta.4

* Tue Dec  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.2.beta3
- 1.5.0.beta.3

* Sun Oct 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.1.beta2
- Try 1.5.0.beta.2

* Fri Jul 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.3.1-1
- 1.4.3.1

* Wed May 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.2-1
- 1.4.2

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-2
- Fix build failure with libxml2 >= 2.7.7

* Tue Dec 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1
- 1.4.1

* Mon Nov  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.0-1
- 1.4.0

* Sat Aug 22 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.3-2
- Fix test failure on sparc

* Wed Jul 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.3-1
- 1.3.3

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-3
- F-12: Mass rebuild

* Thu Jul  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-2
- Enable test
- Recompile with -O2

* Thu Jun 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-1
- 1.3.2

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.1-1
- 1.3.1

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-1
- 1.2.3

* Thu Mar 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.2-1
- 1.2.2

* Thu Mar 12 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-1
- 1.2.1

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-2
- F-11: Mass rebuild

* Thu Jan 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-1
- 1.1.1

* Thu Dec 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.0-1
- Initial packaging

