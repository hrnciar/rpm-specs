%global	gem_name	pdfkit

Name:		rubygem-%{gem_name}
Version:	0.8.4.2
Release:	1%{?dist}

Summary:	HTML+CSS to PDF using wkhtmltopdf
License:	MIT
 
URL:		https://github.com/pdfkit/pdfkit
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	git
BuildRequires:	rubygems-devel

BuildRequires:	wkhtmltopdf
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(mocha)
BuildRequires:	rubygem(simplecov)
BuildRequires:	rubygem(rack)
BuildRequires:	rubygem(rack-test)
BuildRequires:	rubygem(activesupport)
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	iputils
Requires:		wkhtmltopdf
BuildArch:		noarch

%description
Create PDFs using plain old HTML+CSS. Uses wkhtmltopdf
on the back-end which renders HTML using Webkit.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.github \
	.gitignore \
	.rspec \
	.ruby-gemset .ruby-version \
	.travis.yml \
	Gemfile Rakefile \
	POST_INSTALL \
	*.gemspec \
	spec/ \
	%{nil}
popd

%check
disable_test() {
	filename=$1
	shift
	num=$#
	while [ $num -gt 0 ]
	do
		sed -i -e "s|it \(\"$1\"\)|xit \1|" $filename
		shift
		num=$((num - 1))
	done
}

pushd .%{gem_instdir}
# Once test all
xvfb-run -n 99 rspec spec/ || true

disable_test spec/configuration_spec.rb \
	"detects the existance of bundler" \
	%{nil}
ping -w3 www.google.co.jp || \
	disable_test spec/pdfkit_spec.rb \
	"can handle ampersands in URLs" \
	%{nil}


xvfb-run -n 98 rspec spec/
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc	%{gem_docdir}

%changelog
* Sun Apr 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.4.2-1
- 0.8.4.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.4.1-1
- 0.8.4.1

* Tue Feb 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-1
- 0.8.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Sun Aug 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Tue Aug 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.0-1
- 0.8.0

* Sun Aug  9 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-2
- Rewrite

* Thu May 07 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-1
- Initial package
