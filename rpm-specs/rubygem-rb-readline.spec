%global	gem_name	rb-readline

Name:		rubygem-%{gem_name}
Version:	0.5.5
Release:	6%{?dist}

Summary:	Pure-Ruby Readline Implementation
License:	BSD

URL:		http://github.com/ConnorAtherton/rb-readline
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest) >= 5
BuildArch:		noarch

%description
The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

pushd %{buildroot}%{gem_instdir}/
rm -rf \
	Rakefile \
	setup.rb \
	*.gemspec \
	bench/ \
	test/ \
	%{nil}
popd

%check
remove_fail_test() {
	filename=$1
	shift
	num=$#
	while [ $num -gt 0 ]
	do
		if [ ! -f ${filename}.orig ] ; then
			cp -p $filename ${filename}.orig
		fi
		sed -i $filename -e "\@def.*$1@,\@end@d"
		shift
		num=$((num - 1))
	done
}

pushd .%{gem_instdir}
# Once do all tests
ruby -Ilib:.:test -e \
	'Dir.glob("test/test_*.rb").each{|f| require f}' || true

# mock uses pseudo-tty and the following test fails
remove_fail_test test/test_readline.rb test_readline_with_default_parameters_does_not_error

ruby -Ilib:.:test -e \
	'Dir.glob("test/test_*.rb").each{|f| require f}'

find . -name \*.orig | while read f ; do mv $f ${f%.orig} ; done
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/README.md

%{gem_libdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_instdir}/CHANGES
%doc	%{gem_instdir}/examples/
%doc	%{gem_docdir}/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug  4 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.5.5-1
- 0.5.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.4-1
- 0.5.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-1
- 0.5.3

* Mon Mar 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-1
- Initial package
