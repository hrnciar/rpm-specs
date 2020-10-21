%global	gem_name	unf
%if ! (0%{?fedora} >= 19 || 0%{?rhel} >= 9)
%global	rubyabi	1.9.1
%endif

%undefine __brp_mangle_shebangs

Summary:	Wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
Name:		rubygem-%{gem_name}
Version:	0.1.4
Release:	16%{?dist}

License:	BSD
URL:		https://github.com/knu/ruby-unf
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} >= 19 || 0%{?rhel} >= 9
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby
%endif

Requires:	ruby(rubygems) 
Requires:	rubygem(unf_ext) 
BuildRequires:	rubygems-devel 
# %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(shoulda)
BuildRequires:	rubygem(unf_ext)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
This is a wrapper library to bring Unicode Normalization Form support
to Ruby/JRuby.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
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

pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	*.gemspec \
	.gitignore \
	.travis.yml \
	test/ \
	%{nil}
popd


%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 9
sed -i.minitest \
	-e 's|Test::Unit::TestCase|Minitest::Test|' \
	test/*.rb
cat > test/unit.rb << EOF
gem "minitest"
require "minitest/autorun"
EOF

%endif

for f in test/test_*.rb
do
	ruby -Ilib:test:. $f
done
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{gem_libdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files	doc
%doc	%{gem_docdir}

%changelog
* Wed Aug 05 2020 Merlin Mathesius <mmathesi@redhat.com> - 0.1.4-16
- Minor conditional fixes for ELN

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-11
- Remove non-runtime files yet more

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-5
- F-21 shoulda is now 3.5.0, fix test case

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-3
- Use minitest/autorun instead of minitest/unit

* Thu Apr 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-2
- Support Minitest 5.x

* Wed Apr  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-1
- 0.1.4

* Sun Oct 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.3-1
- 0.1.3

* Thu Oct  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-1
- 0.1.2

* Mon Apr 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- 0.1.1

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-1
- 0.1.0

* Sat Jan 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.5-1
- Initial package
