%global	gem_name	syck

Summary:	Gemified version of Syck from Ruby's stdlib
Name:		rubygem-%{gem_name}
Version:	1.4.0
Release:	3%{?dist}

# README.rdoc
License:	MIT
URL:		http://github.com/tenderlove/syck/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

# MRI only
Requires:	ruby
BuildRequires:	ruby

Requires:	ruby(rubygems)
BuildRequires:	gcc
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
# %% check
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}

%description
A gemified version of Syck from Ruby's stdlib.  
Syck has been removed from Ruby's stdlib, and this gem is 
meant to bridge the gap for people that haven't
updated their YAML yet.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# Patch

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec

# Kill syck.bundle
rm -f lib/syck.bundle
sed -i -e \
	's|"lib/syck.bundle",||' \
	%{gem_name}.gemspec

# Kill #line for debuginfo rpm generation
sed -i -e '/^#line/d' \
	ext/syck/*.{c,h}

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%if 0%{?fedora} >= 21
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

%else
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
mv \
	%{buildroot}%{gem_instdir}/lib/%{gem_name}.so \
	%{buildroot}%{gem_extdir_mri}/lib/

%endif

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}

cat > test/helper.rb <<EOF
require 'test/unit'
require 'syck'
EOF

ruby \
%if 0%{?fedora} >= 21
	-Ilib:test:.:ext/%{gem_name} \
%else
	-Ilib:test:. \
%endif
	-e 'Dir.glob( "test/test_*.rb" ).sort.each {|f| require f }' \
	|| echo "need investigating"

popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/.[a-z]*
%exclude	%{gem_instdir}/Rakefile

%{gem_libdir}/
%{gem_extdir_mri}/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%exclude	%{gem_instdir}/test/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-2
- F-32: rebuild against ruby27

* Wed Jan 15 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-1
- 1.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-13
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.5-10
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-9
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-5
- F-26: rebuild for ruby24
- and ruby24 build fix

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-3
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-1
- 1.0.5

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-7
- F-22: Rebuild for ruby 2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-4
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-2
- Add BR: rubygem(minitest) for %%check

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- Initial package
