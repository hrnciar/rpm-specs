%global	gem_name	mini_portile2

Name:		rubygem-%{gem_name}
Version:	2.5.0
Release:	1%{?dist}

Summary:	Simplistic port-like solution for developers
License:	MIT
URL:		http://github.com/flavorjones/mini_portile
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	rubygems-devel
# BuildRequires:	rubygem(minitest)
# BuildRequires:	rubygem(minitest-hooks)
#BuildRequires:	rubygem(archive-tar-minitar)
BuildArch:		noarch

%description
Simplistic port-like solution for developers. It provides a standard and
simplified way to compile against dependency libraries without messing up your
system.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
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

pushd %{buildroot}%{gem_instdir}
rm -rf \
	.concourse.yml \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	appveyor.yml \
	concourse/ \
	*.gemspec \
	test/ \
	%{nil}

%check
# Currently minitest-hooks is not available on Fedora,
# exit
exit 0

# This requires net connection, so give up test suite
# without net
# (also just exit without ping)
ping -w3 fedoraproject.org || exit 0

pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.md
%doc	%{gem_instdir}/CHANGELOG.md

%{gem_libdir}
%{gem_spec}

%exclude	%{gem_cache}

%files	doc
%doc	%{gem_docdir}

%changelog
* Tue Feb 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-1
- 2.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.0-1
- 2.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.0-1
- 2.3.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Wed Dec 09 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-1
- Initial package
