%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global git_url https://raw.githubusercontent.com/jekyll/%{gem_name}/master
%global gem_name mercenary

Name:		rubygem-%{gem_name}
Version:	0.3.6
Release:	8%{?dist}
Summary:	An easier way to build your command-line scripts in Ruby

License:	MIT
URL:		https://github.com/jekyll/%{gem_name}
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch:	noarch
BuildRequires:	rubygems-devel

%description
Lightweight and flexible library for writing command-line apps in Ruby.


%package doc
Summary:	Documentation files for %{name}

%description doc
This package contains the documentation files for %{name}.


%prep
%{__rm} -rf %{gem_name}-%{version}
%{_bindir}/gem unpack %{SOURCE0}
%setup -DTqn %{gem_name}-%{version}
%{_bindir}/gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
/bin/ln LICENSE.txt LICENSE
/bin/ln README.md README.markdown
for f in examples/*.rb
do
	%{__sed} -e '1s:^#![ \t]*%{_bindir}/env ruby:#!%{_bindir}/ruby:'	\
		< ${f} > ${f}.new &&						\
	/bin/touch -r ${f} ${f}.new && %{__mv} -f ${f}.new ${f} &&		\
	%{__chmod} -c 0755 ${f}
done


%build
%{_bindir}/gem build %{gem_name}.gemspec
%gem_install


%install
%{__mkdir} -p %{buildroot}%{gem_dir}
%{__cp} -a ./%{gem_dir}/* %{buildroot}%{gem_dir}
%{__rm} -f %{buildroot}%{gem_instdir}/{*.gemspec,*.md,*.markdown,.travis.yml}
%{__rm} -f %{buildroot}%{gem_instdir}/{.gitignore,.rspec,LICENSE.txt,Rakefile}
%{__rm} -rf %{buildroot}%{gem_instdir}/script


%files
%exclude %{gem_cache}
%license LICENSE
%doc History.markdown README.markdown
%{gem_instdir}
%{gem_spec}

%files doc
%doc %{_pkgdocdir}
%doc %{gem_docdir}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Björn Esser <fedora@besser82.io> - 0.3.6-1
- initial import (#1368848)

* Sun Aug 21 2016 Björn Esser <fedora@besser82.io> - 0.3.6-0.1
- initial rpm-release (#1368848)
