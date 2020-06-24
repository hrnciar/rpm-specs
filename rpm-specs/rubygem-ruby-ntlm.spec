%global	gem_name	ruby-ntlm

%if 0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif

%if 0%{?fedora} >= 21
%global	gem_minitest	rubygem(minitest4)
%else
%global	gem_minitest	rubygem(minitest)
%endif

Summary:	NTLM implementation for Ruby
Name:		rubygem-%{gem_name}
Version:	0.0.4
Release:	7%{?dist}

# README.markdown
License:	MIT
URL:		http://github.com/macks/ruby-ntlm
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	rubygem-ruby-ntlm-0.0.1-test-suite-is-binary.patch

%if 0%{?fedora} >= 19
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby 
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby 
%endif

Requires:	ruby(rubygems)
Requires:	ruby
BuildRequires:	rubygems-devel 
BuildRequires:	rubygem(test-unit)
BuildRequires:	ruby
# %%check
BuildRequires:	%gem_minitest

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
NTLM implementation for Ruby.


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

%patch0 -p1

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
rm -f \
	.gitignore \
	.travis.yml \
	*gemspec \
	%{nil}

%check
pushd .%{gem_instdir}
ruby -Ilib:test:. -e 'Dir.glob("test/*_test.rb").each{|f| require f}'
popd


%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile

%{gem_libdir}
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/examples/
%exclude	%{gem_instdir}/test/
%exclude	%{gem_instdir}/unused/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.4-1
- 0.0.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.3-1
- 0.0.3

* Fri Feb  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.1-9
- Use %%gem_install

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.1-7
- BR: rubygem(test-unit)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.1-5
- Force to use minitest ver4 for now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.1-2
- F-19: rebuild for ruby 2.0.0

* Sun Jan 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.1-1
- Initial package
