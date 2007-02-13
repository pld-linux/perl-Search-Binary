%include	/usr/lib/rpm/macros.perl
%define		pdir	Search
%define		pnam	Binary
Summary:	Search::Binary Perl module
Summary(cs.UTF-8):	Modul Search::Binary pro Perl
Summary(da.UTF-8):	Perlmodul Search::Binary
Summary(de.UTF-8):	Search::Binary Perl Modul
Summary(es.UTF-8):	Módulo de Perl Search::Binary
Summary(fr.UTF-8):	Module Perl Search::Binary
Summary(it.UTF-8):	Modulo di Perl Search::Binary
Summary(ja.UTF-8):	Search::Binary Perl モジュール
Summary(ko.UTF-8):	Search::Binary 펄 모줄
Summary(nb.UTF-8):	Perlmodul Search::Binary
Summary(pl.UTF-8):	Moduł Perla Search::Binary
Summary(pt.UTF-8):	Módulo de Perl Search::Binary
Summary(pt_BR.UTF-8):	Módulo Perl Search::Binary
Summary(ru.UTF-8):	Модуль для Perl Search::Binary
Summary(sv.UTF-8):	Search::Binary Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Search::Binary
Summary(zh_CN.UTF-8):	Search::Binary Perl 模块
Name:		perl-Search-Binary
Version:	0.95
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b75a99c0dedd05cb455686fc547cc78f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Search::Binary - generic binary search.

%description -l pl.UTF-8
Search::Binary - podstawowe wyszukiwanie binarne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Search
%{_mandir}/man3/*
