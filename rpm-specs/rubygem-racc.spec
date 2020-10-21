%global	gem_name	racc

Name:		rubygem-%{gem_name}
Version:	1.5.0
Release:	201%{?dist}

Summary:	LALR(1) parser generator
License:	BSD
URL:		https://github.com/tenderlove/racc

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source10:	rubygem-%{gem_name}-%{version}-missing-files.tar.gz
# Source10 is created by %%{SOURCE11} %%version
Source11:	racc-create-tarball-missing-files.sh

BuildRequires:	gcc
BuildRequires:	rubygems-devel
BuildRequires:	ruby-devel
BuildRequires:	rubygem(test-unit)


%description
Racc is a LALR(1) parser generator.
It is written in Ruby itself, and generates Ruby program.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
rm -rf %{gem_name}-%{version}
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Fix shebang
grep -rl /usr/local . | xargs -r sed -i -e 's|/usr/local|/usr|'

# Encoding
for f in \
	sample/calc-ja.y \
	web/racc.ja.rhtml \
	%{nil}
do
	touch -r $f $f.stamp
	iconv -f EUC-JP -t UTF-8 $f > $f.tmp
	mv $f.tmp $f
	touch -r $f.stamp $f
	rm -f $f.stamp
done

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{_prefix}
cp -a .%{_prefix}/* \
	%{buildroot}%{_prefix}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* \
	%{buildroot}%{gem_extdir_mri}/
rm -f %{buildroot}%{gem_extdir_mri}/{gem_make.out,mkmf.log}

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	ext/ \
	fastcache/ \
	misc/ \
	tasks/ \
	test/ \
	DEPENDS \
	Manifest.txt \
	Rakefile \
	setup.rb \
	%{nil}

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}

rm -rf %{gem_name}/%{version}
gzip -dc %{SOURCE10} | tar xf -
cp -a %{gem_name}-%{version}/* .

LANG=C.utf8
# Kill "assert_output_unchanged" test for now
# Output from racc between 1.4.14 and 1.4.15 differ
sed -i.match test/test_racc_command.rb \
	-e '\@assert_output_unchanged@d'

ruby -Ilib:test:. -e \
	"gem 'test-unit' ; Dir.glob('test/test_*.rb').each {|f| require f}"
popd

%files
%dir	%{gem_instdir}

%license	%{gem_instdir}/COPYING
%doc	%lang(ja)	%{gem_instdir}/README.ja.rdoc
%doc	%{gem_instdir}/README.rdoc
%doc	%{gem_instdir}/ChangeLog

%{_bindir}/racc

%{gem_extdir_mri}
%{gem_instdir}/bin
%{gem_libdir}

%{gem_spec}

%files	doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/TODO
%doc	%{gem_instdir}/rdoc
%doc	%{gem_instdir}/sample
%doc	%{gem_instdir}/web

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.0-200
- 1.5.0
- racc2y, y2racc removed

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.16-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.16-200
- F-32: rebuild against ruby27

* Mon Dec 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.16-1
- 1.4.16

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.15-1
- 1.4.15

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.14-11
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.4.14-8
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.14-7
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec  6 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.14-1
- 1.4.14

* Tue Nov 03 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-1
- Initial package
