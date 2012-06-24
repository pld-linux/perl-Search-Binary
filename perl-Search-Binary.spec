%include	/usr/lib/rpm/macros.perl
%define		pdir	Search
%define		pnam	Binary
Summary:	Search::Binary Perl module
Summary(cs):	Modul Search::Binary pro Perl
Summary(da):	Perlmodul Search::Binary
Summary(de):	Search::Binary Perl Modul
Summary(es):	M�dulo de Perl Search::Binary
Summary(fr):	Module Perl Search::Binary
Summary(it):	Modulo di Perl Search::Binary
Summary(ja):	Search::Binary Perl �⥸�塼��
Summary(ko):	Search::Binary �� ����
Summary(no):	Perlmodul Search::Binary
Summary(pl):	Modu� Perla Search::Binary
Summary(pt):	M�dulo de Perl Search::Binary
Summary(pt_BR):	M�dulo Perl Search::Binary
Summary(ru):	������ ��� Perl Search::Binary
Summary(sv):	Search::Binary Perlmodul
Summary(uk):	������ ��� Perl Search::Binary
Summary(zh_CN):	Search::Binary Perl ģ��
Name:		perl-Search-Binary
Version:	0.95
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Search::Binary - generic binary search.

%description -l pl
Search::Binary - podstawowe wyszukiwanie binarne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Search
%{_mandir}/man3/*
