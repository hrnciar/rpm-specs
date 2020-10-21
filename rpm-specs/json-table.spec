Name:           json-table
Version:        4.3.3
Release:        4%{?dist}
Summary:        Command-line tool to transform nested JSON into tabular data

License:        EPL-1.0
URL:            https://github.com/micha/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
Jt reads UTF-8 encoded JSON forms from stdin and writes tab separated values
(or CSV) to stdout. A simple stack-based programming language is used to
extract values from the JSON input for printing.

%prep
%autosetup
sed -i -e /-static/d -e '/PREFIX :=/d' Makefile

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{buildroot}%{_prefix}

%check
make test

%files
%license LICENSE
%doc README.md
%doc *.html *.css *.ronn
%{_bindir}/jt
%{_mandir}/man1/jt.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.3.3-3
- Update URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Raphael Groner <projects.rg@smart.ms> - 4.3.3-1
- initial
